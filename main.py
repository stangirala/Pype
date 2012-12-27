import subprocess
import sys

def createChildTester(inputScript, inputData):
"""This function does the actual testing. I tried writing this without communicate, cause this is a non-blocking way of doing it. That is, without .stdin.write, .stdout.read and .stderr.read."""

  cmd = ["python", inputScript]

  tempFile = open(inputData, 'r')

  inputs = []

  for line in tempFile:
    line.strip('\n')

    child = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

    inputs = line.split()

    # Read number of inputs
    NumberOfInputs = inputs[0]

    commsstring = ""
    for i in range(int(NumberOfInputs)):
      commsstring += inputs[i + 1]
      if i < NumberOfInputs:
        commsstring += "\n"
    print "Comms string: ", commsstring

    commsout, commserr = child.communicate(commsstring)

    print "Commsout: ", commsout

    commsout.strip('\n')
    commsout.strip(' ')

    if (int(commsout) == int(inputs[int(NumberOfInputs) + 1])):
      print "Passed"
    else:
      print "Failed. Required Answer is " + str(inputs[int(NumberOfInputs) + 1])

  return child


if __name__ == '__main__':

  if len(sys.argv) > 1 and len(sys.argv) == 3:
    input = sys.argv[1]

  if len(sys.argv) == 1 or len(sys.argv) == 2:
    if len(sys.argv) == 2:
      print "Insuficient input. Enter again.\n"
    inputScript = raw_input("Enter script file name\n")
    inputData = raw_input("\nEnter data file name\n")

  print '\n'

  newChild = createChildTester(inputScript, inputData)

  code = newChild.returncode

  if (code != 0):
    print "Something went wrong " + str(code)
