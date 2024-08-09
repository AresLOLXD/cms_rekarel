from cms.grading.language import Language
from abc import abstractmethod

import logging

logger = logging.getLogger(__name__)

class KarelLanguage(Language):


    @property
    def name(self):
        return "Karel (rekarel.1.0.0)"
    
    
    @property
    def source_extensions(self):
        return [".kcode", ".kc", ".kj", ".kp", ".txt"]
    
    @property
    def executable_extension(self):
        return ".kx"
    
    @property
    def requires_multithreading(self):
        return True

    def get_compilation_commands(self, source_filenames, executable_filename, for_evaluation=True):        
        command = ["/usr/local/bin/rekarel"]
        command += ["compile"]
        print(source_filenames)
        command += source_filenames
        command += ["-o", executable_filename]
        return [command ]

    def get_evaluation_commands(self, executable_filename, main=None, args=None):     
        command = ["/usr/local/bin/karel"]
        # command += ["run"]
        command += [ executable_filename ]
        # command += ["-i", "world.in"]
        # command += ["-o", "world.out"]
        logger.warn(command)
        return [command]

class KarelPascal(KarelLanguage):
    @property
    def name(self):
        return "Karel Pascal (rekarel.1.0.0)"

    @property
    def source_extensions(self):
        return [".kp"]

class KarelJava(KarelLanguage):

    @property
    def name(self):
        return "Karel Java (rekarel.1.0.0)"

    @property
    def source_extensions(self):
        return [".kj"]
