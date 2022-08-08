import fuzzyReader

path = "fis.fis"
# pass "generalizedbell" or "gaussbell"
function_type="generalizedbell"
input1 = 3000
input2 = 200

# pass false or default to silent to print info about generated fuzzy system
fr = fuzzyReader.FuzzyReader(path, function_type, silent=False)

fuzzy_system = fr.read()

fuzzy_system.set_variable("input1", input1)
fuzzy_system.set_variable("input2", input2)
result = fuzzy_system.Sugeno_inference(["Output"])['Output']

print(result)