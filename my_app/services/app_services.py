import os
from my_app.domain.application_state import ApplicationState
from my_app.domain.pokedex_types import Pokemon
from my_app.infrastructure.exe_utils import ExeResult, execute_external_cmd
from my_app.infrastructure.pokedex_json_parser import PokedexJsonReader

class ApplicationServices:
    
    def __init__(self, app_title: str, app_version: str) -> None:
        self.app_state: ApplicationState = ApplicationState(app_version, app_title)

    def get_pokedex_data(self) -> list[Pokemon]:

        local_file_dir = os.path.dirname(os.path.realpath(__file__)) 
        data_file_path = os.path.join(local_file_dir, "..", "..", "test", "data", "pokedex.json")       
        reader = PokedexJsonReader()
        return reader.parse(data_file_path)
    
    def run_external_cmd(self, cmd_array: list[str]) -> ExeResult:
        return execute_external_cmd(cmd_array)