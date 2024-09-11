import sys
import random

class VulnerableClass:
    def __init__(self, data):
        self.data = data

    def unsafe_memory_access(self):
        """Simulate unsafe memory access"""
        if len(self.data) > 100:
            print("Simulated memory corruption! Data size too large!")
            raise MemoryError("Memory corruption detected!")

    def use_after_free(self):
        """Simulate use-after-free vulnerability by deleting and then accessing an object"""
        print("Simulating use-after-free...")
        temp = self.data
        del self.data
        try:
            # Simulating a use-after-free by accessing data after deletion
            print("Accessing data after deletion:", temp[0])
        except Exception as e:
            print("Caught error (use-after-free simulated):", e)

    def type_confusion(self, index):
        """Simulate type confusion"""
        try:
            print("Attempting type confusion...")
            result = self.data[index] + "confusion"
            print("Result:", result)
        except Exception as e:
            print("Caught type confusion error:", e)

    def execute(self):
        self.unsafe_memory_access()
        if "usefree" in self.data:
            self.use_after_free()
        if "confuse" in self.data:
            self.type_confusion(0)
        return "Execution completed without major issues."

def vulnerable_function(input_string):
    # Initialize the vulnerable class with the input string
    vc = VulnerableClass(input_string)

    # Execute its potentially vulnerable methods
    result = vc.execute()
    print(result)

def main():
    if len(sys.argv) != 2:
        print("Usage: python advanced_vulnerable_program.py <input>")
        return

    input_string = sys.argv[1]

    try:
        vulnerable_function(input_string)
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    main()
