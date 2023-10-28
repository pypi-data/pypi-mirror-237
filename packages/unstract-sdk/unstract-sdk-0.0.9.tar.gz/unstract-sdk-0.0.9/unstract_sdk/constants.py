class PlatformServiceKeys:
    PLATFORM_API_KEY = "PLATFORM_API_KEY"


class ConnectorKeys:
    ID = "id"
    PROJECT_ID = "project_id"
    CONNECTOR_ID = "connector_id"
    TOOL_INSTANCE_ID = "tool_instance_id"
    CONNECTOR_METADATA = "connector_metadata"
    CONNECTOR_TYPE = "connector_type"


class ConnectorType:
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"


class Connector:
    FILE_SYSTEM = "FILE_SYSTEM"
    DATABASE = "DATABASE"


class Command:
    SPEC = "SPEC"
    PROPERTIES = "PROPERTIES"
    ICON = "ICON"
    RUN = "RUN"
    VARIABLES = "VARIABLES"

    @classmethod
    def static_commands(cls) -> set[str]:
        return {cls.SPEC, cls.PROPERTIES, cls.ICON, cls.VARIABLES}
