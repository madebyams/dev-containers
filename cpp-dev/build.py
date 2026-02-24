#!python3
import os
from pathlib import Path
import subprocess
import shutil

paths = [
    "build",
    "CMakeUserPresets.json"
]

def build():
    try:
        for path in paths:
            file_path = Path(path) 
            if file_path.exists():
                shutil.rmtree(file_path) if file_path.is_dir() else os.remove(file_path)

        subprocess.run(["conan", "install", ".", "--output-folder=build", "--build=missing"], check=True)
        shutil.copy("./build/build/Release/generators/conan_toolchain.cmake", ".")
        generators_path = str(Path("build/build/Release/generators").absolute())
        subprocess.run(['cmake' ,'-S', '.', '-B', 'build', '-G', "Ninja", '-DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake', f'-DCMAKE_PREFIX_PATH={generators_path}', '-DCMAKE_BUILD_TYPE=Release'], check=True)
        subprocess.run(["cmake", "--build", "build", "--config", "Release"], check=True)
        return True 
    
    except subprocess.CalledProcessError:
        return False

if __name__ == '__main__':
    build()