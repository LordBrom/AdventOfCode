from functools import lru_cache
import time

ADAPTERS = []
ADAPTERS_RESULTS = []

@lru_cache(maxsize = None)
def check_adapters(pointer):

	if pointer == len(ADAPTERS) - 1:
		return 1

	count = 0
	if pointer + 1 < len(ADAPTERS) and ADAPTERS[pointer + 1] - ADAPTERS[pointer] <= 3:
		count += check_adapters(pointer + 1)

	if pointer + 2 < len(ADAPTERS) and ADAPTERS[pointer + 2] - ADAPTERS[pointer] <= 3:
		count += check_adapters(pointer + 2)

	if pointer + 3 < len(ADAPTERS) and ADAPTERS[pointer + 3] - ADAPTERS[pointer] <= 3:
		count += check_adapters(pointer + 3)

	return count

inFile = open("day10.in", "r").read().split("\n")
inFile.pop()

inFile = open("day10.in", "r").read().split("\n")
inFile.pop()

for i in range(len(inFile)):
	ADAPTERS_RESULTS.append("")
	inFile[i] = int(inFile[i])

ADAPTERS_RESULTS.append("")
ADAPTERS_RESULTS.append("")
ADAPTERS = [0] + sorted(inFile) + [max(inFile) + 3]

begin = time.time()
result = check_adapters(0)
end = time.time()

print(result)
