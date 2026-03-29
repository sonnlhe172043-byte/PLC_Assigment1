def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class Memory:

    def __init__(self) -> None:
        
        self.memory: dict = {}

    def get(self, variable_name: str):
        assert variable_name in self.memory, f"{variable_name} not exist in Memory"
        return self.memory[variable_name]["value"]

    def get_data(self, variable_name: str):
        """Return full data (value + type) if needed"""
        assert variable_name in self.memory
        return self.memory[variable_name]

    def set(self, variable_name: str, value, data_type):
        # crash if variable already exists
        assert variable_name not in self.memory, f"{variable_name} already exists"
        self.memory[variable_name] = {
            "value": value,
            "data_type": data_type
        }

    def update(self, variable_name: str, value):
        """Update variable value"""
        assert variable_name in self.memory, f"{variable_name} not exist"
        self.memory[variable_name]["value"] = value

    def __repr__(self) -> str:
        string = ""
        string += "Name\tValue\tData Type\n"
        string += "-" * 30 + "\n"

        for var, data in self.memory.items():
            string += f"{var}\t{data['value']}\t{data['data_type']}\n"

        string += "-" * 30 + "\n"
        return string


if __name__ == "__main__":
    memory = Memory()

    memory.set(variable_name='a', value=10, data_type=int)
    memory.set(variable_name='b', value="20", data_type=str)

    print(memory)

    print(memory.get("b"))        # just value
    print(memory.get_data("b"))   # just info info