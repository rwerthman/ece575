from CPU import CPU

def main():
    instructionMemory = [ "instruction1", "instruction2" ]
    cpu = CPU( instructionMemory )
    cpu.cycle()

if __name__ == "__main__":
    main()
