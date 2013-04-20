
import sys
minor = sys.version.split('.')[1]
if minor == '2':
    import seahaven_cpython_3_2
elif minor == '3':
    import seahaven_cpython_3_3

