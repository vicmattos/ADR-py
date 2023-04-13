from dataclasses import dataclass

from adrpy.injection import Inject
from adrpy.services.file.base import BaseFileService
from adrpy.services.template.base import BaseTemplateService
from adrpy.shared_kernel.dtos import CreateADRDTO
from adrpy.shared_kernel.settings import Settings


@dataclass
class CreatingADR:
    template_service: Inject[BaseTemplateService]
    file_service: Inject[BaseFileService]
    settings: Inject[Settings]

    def execute(self, dto: CreateADRDTO) -> None:
        app_template_file = self.file_service.get_file(path=dto.adr_template_path)
        rendered_template = self.template_service.render(
            template_file=app_template_file,
            data={"date": "TODAY", "status": "ACCEPTED", "name": dto.name, "ordinal_num": 1},
        )
        self.file_service.create_file(
            path=self.settings.adr_dir,  # TODO: Handle missing dir
            filename=dto.adr_name_with_ordinal(ordinal_number=2),
            content=rendered_template.content,
        )
