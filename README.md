CCS project configurations:
===========================

To find the driverlib files, add the PATH of the tivaware repository in the include paths:
Properties -> Build -> ARM compiler options -> Include Options -> Add dir to #include search paths

Increase the stack size to 25000:
Build -> ARM linker -> Basic options -> Set C system stack size

To generate a bin file using the CCS build add the following commands to the Build post-compile steps in 
the CCS enviroment:
Properties -> Build -> Steps -> Post-build steps
"${CCE_INSTALL_ROOT}/utils/tiobj2bin/tiobj2bin" "${BuildArtifactFileName}" "${BuildArtifactFileBaseName}.bin" "${CG_TOOL_ROOT}/bin/armofd" "${CG_TOOL_ROOT}/bin/armhex" "${CCE_INSTALL_ROOT}/utils/tiobj2bin/mkhex4bin"



LM4TOOLS[https://github.com/utzig/lm4tools]: Tools to load program onto the Tiva.
Use the lm4flash tools to load the program on teh Tiva from the Raspberry-pi (or any other SBC/PC).
Note: You might need to use "sudo" to obtain access to the port on the Raspberry-pi.
Command : ./lm4flash <file_name>.bin -S /dev/ttyACM0

