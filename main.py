from src.CPU import CPU

def main():
    instructionMemory = [
        [ "add", "r1", "r2", "r3" ],
    ]

    cpu = CPU( instructionMemory )
    cpu.cycle()

if __name__ == "__main__":
    main()
