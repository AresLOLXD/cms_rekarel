from cms.grading.tasktypes.Batch import Batch
from cms.grading.steps.messages import HumanMessage
# Dummy function to mark translatable strings



import logging
import os

from cms.grading.languagemanager import LANGUAGES, get_language
from cms.grading.steps import evaluation_step, \
    human_evaluation_message
from cms.grading.tasktypes import check_executables_number, \
    create_sandbox, delete_sandbox, eval_output
from cms.grading.Sandbox import Sandbox

logger = logging.getLogger(__name__)

def N_(message):
    return message



class KarelTask(Batch):

    def __init__(self, parameters):
        super().__init__(parameters)

    @property
    def name(self):
        return "Karel"
    
    def evaluate(self, job, file_cacher):        
        """Implements mostrly Batch.evaluate. See TaskType.evaluate."""
        if not check_executables_number(job, 1):
            return

        # Prepare the execution
        executable_filename = next(iter(job.executables.keys()))
        language = get_language(job.language)
        main = self.GRADER_BASENAME if self._uses_grader() \
               else os.path.splitext(executable_filename)[0]
        commands = language.get_evaluation_commands(
            executable_filename, main=main)
        executables_to_get = {
            executable_filename: job.executables[executable_filename].digest
        }
        files_to_get = {
            self._actual_input: job.input
        }

        # Check which redirect we need to perform, and in case we don't
        # manage the output via redirect, the submission needs to be able
        # to write on it.
        files_allowing_write = []
        stdin_redirect = None
        stdout_redirect = None
        if len(self.input_filename) == 0:
            stdin_redirect = self._actual_input
        if len(self.output_filename) == 0:
            stdout_redirect = self._actual_output
        else:
            files_allowing_write.append(self._actual_output)

        # Create the sandbox
        sandbox = create_sandbox(file_cacher, name="evaluate")
        job.sandboxes.append(sandbox.get_root_path())

        # Put the required files into the sandbox
        for filename, digest in executables_to_get.items():
            sandbox.create_file_from_storage(filename, digest, executable=True)
        for filename, digest in files_to_get.items():
            sandbox.create_file_from_storage(filename, digest)

        # Actually performs the execution
        box_success, evaluation_success, stats = evaluation_step(
            sandbox,
            commands,
            job.time_limit,
            job.memory_limit,
            writable_files=files_allowing_write,
            stdin_redirect=stdin_redirect,
            stdout_redirect=stdout_redirect,
            multiprocess=job.multithreaded_sandbox)

        outcome = None
        text = None

        # Error in the sandbox: nothing to do!
        if not box_success:
            pass

        # Contestant's error: the marks won't be good
        elif not evaluation_success:
            outcome = 0.0
            text = human_evaluation_message(stats)
            if job.get_output:
                job.user_output = None

        # Otherwise, advance to checking the solution
        else:

            # Check that the output file was created
            if not sandbox.file_exists(self._actual_output):
                outcome = 0.0
                text = [N_("Evaluation didn't produce file %s"),
                        self._actual_output]
                if job.get_output:
                    job.user_output = None

            else:
                # If asked so, put the output file into the storage.
                if job.get_output:
                    job.user_output = sandbox.get_file_to_storage(
                        self._actual_output,
                        "Output file in job %s" % job.info,
                        trunc_len=100 * 1024)

                # If just asked to execute, fill text and set dummy outcome.
                if job.only_execution:
                    outcome = 0.0
                    text = [N_("Execution completed successfully")]

                # Otherwise evaluate the output file.
                else:
                    box_success, outcome, text = eval_output(
                        file_cacher, job,
                        self.CHECKER_CODENAME
                        if self._uses_checker() else None,
                        user_output_path=sandbox.relative_path(
                            self._actual_output),
                        user_output_filename=self.output_filename)

        # Fill in the job with the results.
        job.success = box_success
        job.outcome = str(outcome) if outcome is not None else None
        job.text = text
        if (stats["exit_status"] == Sandbox.EXIT_NONZERO_RETURN):
            exit_signal = sandbox.get_exit_code()            
            if exit_signal == 16:
                job.text = [N_("Error de ejecución (Karel chocó con un muro)")]
            elif exit_signal == 17:
                job.text = [N_("Error de ejecución (Karel intentó recoger un zumbador de una posición vacía)")]
            elif exit_signal == 18:
                job.text = [N_("Error de ejecución (Karel intentó dejar un zumbador con su mochila vacía)")]
            elif exit_signal == 19:
                job.text = [N_("Error de ejecución (La pila de llamadas se desbordó)")]
            elif exit_signal == 20:
                job.text = [N_("Error de ejecución (Se excedió la memoria de la pila de llamadas)")]
            elif exit_signal == 21:
                job.text = [N_("Error de ejecución (Se excedió la cantidad de parámetros permitidos en una llamada)")]
            elif exit_signal == 48:
                job.text = [N_("Límite de instrucciones excedido (Demasiadas en general)")]
            elif exit_signal == 49:
                job.text = [N_("Límite de instrucciones excedido (Demasiadas izquierdas)")]
            elif exit_signal == 50:
                job.text = [N_("Límite de instrucciones excedido (Demasiados avanzas)")]
            elif exit_signal == 51:
                job.text = [N_("Límite de instrucciones excedido (Demasiados coge-zumbadores)")]
            elif exit_signal == 52:
                job.text = [N_("Límite de instrucciones excedido (Demasiados deja-zumbadores)")]
        job.plus = stats

        delete_sandbox(sandbox, job.success, job.keep_sandbox)
