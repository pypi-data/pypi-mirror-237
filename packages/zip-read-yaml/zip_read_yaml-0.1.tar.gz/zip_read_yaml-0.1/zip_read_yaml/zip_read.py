import zipfile
import yaml
import typing as t
from pathlib import Path
import os


def check_yaml_exists(dir_path: t.Union[Path, str], out_file: str):
    """
    Create new YAML file with out_file as its name, which will contain all YAML from zip files.
    :param dir_path: Path to Directory containing zip files
    :param out_file: New YAML file
    :return:
    """
    check_file = os.path.exists(dir_path.joinpath(out_file))
    if check_file:
        pass
    else:
        with open(dir_path.joinpath(out_file), mode="w") as yaml_file:
            yaml.safe_dump('{}', yaml_file)
    return


def read_yaml_zip(dir_path: t.Union[Path, str], yaml_name: str, out_file: str) -> None:
    """
    Read a YAML file from the given directory and combines them into a new YAML file.
    :param dir_path: Path to the directory containing zip files
    :param yaml_name: Yaml file that needs to be read from zip files
    :param out_file: New file that containes aggregated yaml content from all the zip files
    :return:
    """
    zip_files = os.listdir(dir_path)
    for count, file in enumerate(zip_files):
        yaml_read_zip = zipfile.ZipFile(dir_path.joinpath(file), 'r')
        yaml_file = yaml_read_zip.read(yaml_name)
        key_name = f'key_{str(count)}'
        yaml_decode = yaml_file.decode('utf8').replace("'", '"')
        yaml_final = yaml.safe_load(yaml_decode)
        check_yaml_exists(dir_path, out_file)
        with open(dir_path.joinpath(out_file), "r") as yaml_file:
            cur_yaml = yaml.safe_load(yaml_file)
            new_yaml_content = {key_name: yaml_final}
            if new_yaml_content:
                with open(dir_path.joinpath(out_file), "w") as update_yaml:
                    yaml.safe_dump(new_yaml_content, update_yaml)
    return


if __name__=="__main__":
    current_dir = Path(__file__).absolute().parent.parent
    zip_dir = current_dir.joinpath('zip_folders')
    read_yaml_zip(zip_dir, "test.yaml", "new_test.yaml")
