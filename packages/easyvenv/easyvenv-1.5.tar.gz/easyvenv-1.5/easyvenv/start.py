import os
import subprocess
import sys
import json
import pkg_resources


def create_folder_structure(path: str = None):
    if path is None:
        path = os.path.dirname(__file__)

    # Make main folders
    scripts_path = os.path.join(path, "scripts")
    os.makedirs(scripts_path, exist_ok=True)
    venv_path = os.path.join(path, "venv")
    os.makedirs(venv_path, exist_ok=True)
    resources_path = os.path.join(path, "resources")
    os.makedirs(resources_path, exist_ok=True)
    managing_path = os.path.join(path, "managing")
    os.makedirs(managing_path, exist_ok=True)

    # Manage prev requirements
    prev_requirements_path = os.path.join(
        managing_path, "prev_requirements.txt")

    prev_requirements_exists = os.path.exists(prev_requirements_path)
    if not prev_requirements_exists:
        with open(prev_requirements_path, "w") as prev_req_file:
            prev_req_file.write("")

    dist = pkg_resources.get_distribution("easyvenv")

    name, version = str(dist).split(" ")

    self_requirement = f"{name}=={version}"

    # Manage current requirements
    requirements_path = os.path.join(
        path, "requirements.txt")

    requirements_exists = os.path.exists(requirements_path)
    if not requirements_exists:
        with open(requirements_path, "w") as req_file:
            req_file.write(f"""{self_requirement}
twine""")

    # Manage main script
    main_script_path = os.path.join(
        scripts_path, "main.py")

    main_script_exists = os.path.exists(main_script_path)
    if not main_script_exists:
        with open(main_script_path, "w") as main_file:
            main_file.write('print("Hello World!")')

    return (path, prev_requirements_path, requirements_path, scripts_path, venv_path, resources_path, managing_path, main_script_path)


def create_venv(path, managing_path):
    venv_path = os.path.join(path, 'venv')
    venv_lock_path = os.path.join(managing_path, 'venv_lock.txt')
    if not os.path.exists(venv_lock_path):
        venv_creation_progress_file_path = os.path.join(
            path, 'venv_is_being_created.txt')
        with open(venv_creation_progress_file_path, "w") as venv_creation_progress_file:
            venv_creation_progress_file.write(
                "The venv is being created. This file will be removed once its finished!")

        with open(venv_lock_path, "w") as venv_lock_file:
            venv_lock_file.write(
                "Venv has been initiated and can't be initiated again unless you remove this lock file. Make sure you know what your doing here!")

        subprocess.check_call([sys.executable, '-m', 'venv', venv_path])

        if os.path.exists(venv_creation_progress_file_path):
            os.remove(venv_creation_progress_file_path)
    return venv_path


def handle_requirements(venv_path, prev_requirements_path, requirements_path):
    # Read the new requirements file
    with open(requirements_path, "r") as requirements:
        new_requirements = set(requirements.read().splitlines())

    # Read the previous requirements file
    with open(prev_requirements_path, "r") as prev_requirements:
        prev_requirements = set(prev_requirements.read().splitlines())

    # Calculate packages to install (in new but not in prev)
    packages_to_install = new_requirements - prev_requirements

    # Calculate packages to uninstall (in prev but not in new)
    packages_to_uninstall = prev_requirements - new_requirements

    if packages_to_install:
        # Install new packages individually
        activation_script = os.path.join(venv_path, 'Scripts', 'activate')
        for package in packages_to_install:
            install_command = f"{activation_script} && pip install {package}"
            subprocess.run(install_command, shell=True)

    if packages_to_uninstall:
        # Uninstall packages that are no longer needed one by one
        activation_script = os.path.join(venv_path, 'Scripts', 'activate')
        for package in packages_to_uninstall:
            uninstall_command = f"{activation_script} && pip uninstall {package} -y"
            subprocess.run(uninstall_command, shell=True)

    # Update the prev_requirements.txt file
    with open(prev_requirements_path, "w") as prev_requirements_file:
        prev_requirements_file.write("\n".join(new_requirements))

    if packages_to_install or packages_to_uninstall:
        print("Package installation and uninstallation complete.")


def run_script_with_venv(venv_path, script_path):
    script_path = os.path.abspath(script_path)
    activation_script = os.path.join(venv_path, 'Scripts', 'activate')
    command = f"{activation_script} && python {script_path}"

    subprocess.run(command, shell=True)


def easyvenv(setup_file_path: str):
    if setup_file_path == "":
        raise Exception("Setup path required. Can't be empty!")

    if not os.path.exists(setup_file_path):
        raise FileExistsError(
            f"Setup path does not exist or is invalid: [{setup_file_path}]")
    path, prev_requirements_path, requirements_path, scripts_path, venv_path, resources_path, managing_path, main_script_path = create_folder_structure(
        setup_file_path)
    create_venv(path, managing_path)
    handle_requirements(venv_path, prev_requirements_path, requirements_path)
    run_script_with_venv(venv_path, main_script_path)


if __name__ == "__main__":
    easyvenv(__file__)
