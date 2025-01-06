from cms.grading.language import Language
from abc import abstractmethod

import logging

logger = logging.getLogger(__name__)
VERSION = "2.3"

class KarelLanguage(Language):
    @property
    def name(self):
        return f"Karel {VERSION} / rekarel-cli"
    
    
    @property
    def source_extensions(self):
        return [".kcode", ".kc", ".kj", ".kp", ".txt"]
    
    @property
    def executable_extension(self):
        return ".kx"
    
    @property
    def requires_multithreading(self):
        return True
    
    
    @property
    def checksKarelVersion(self):
        return True

    def get_compilation_commands(self, source_filenames, executable_filename, for_evaluation=True):        
        command = ["/usr/local/bin/rekarel"]
        command += ["compile"]
        command += source_filenames
        command += ["-o", executable_filename]
        if self.checksKarelVersion:
            command += ["-e", VERSION]
        return [command ]

    def get_evaluation_commands(self, executable_filename, main=None, args=None):     
        command = ["/usr/local/bin/karel"]
        # command += ["run"]
        command += [ executable_filename ]
        if self.checksKarelVersion:
            command += [ "-e", VERSION ]
        # command += ["-i", "world.in"]
        # command += ["-o", "world.out"]
        return [command]

class KarelPascal(KarelLanguage):
    @property
    def name(self):
        return f"Karel Pascal {VERSION} / rekarel-cli"

    @property
    def source_extensions(self):
        return [".kp"]

class KarelJava(KarelLanguage):

    @property
    def name(self):
        return f"Karel Java {VERSION} / rekarel-cli"

    @property
    def source_extensions(self):
        return [".kj"]

class OldKarelLanguage(KarelLanguage):
    """
        Deprecated, this is kept for compatibility and it will be kept until august 2025
    """
    @property
    def name(self):
        return "Karel (rekarel.1.0.0)"
    
    
    @property
    def checksKarelVersion(self):
        # This ensures compatibility with old compilers and runtimes
        return False