################################################################################
# Automatically-generated file. Do not edit!
################################################################################

CG_TOOL_ROOT := /home/sashank/ti/ccs901/ccs/tools/compiler/ti-cgt-arm_18.12.1.LTS

GEN_OPTS__FLAG := 
GEN_CMDS__FLAG := 

ORDERED_OBJS += \
"./bezier.obj" \
"./bezier_test.obj" \
"./main.obj" \
"./main2.obj" \
"./tm4c123gh6pm_startup_ccs.obj" \
"./Peripherals/adc.obj" \
"./Peripherals/cpu.obj" \
"./Peripherals/gpio.obj" \
"./Peripherals/interrupt.obj" \
"./Peripherals/pwm.obj" \
"./Peripherals/sysctl.obj" \
"./Peripherals/timer.obj" \
"./Peripherals/uart.obj" \
"./Peripherals/uartstdio.obj" \
"../tm4c123gh6pm.cmd" \
$(GEN_CMDS__FLAG) \
-llibc.a \
-l"/home/sashank/Stoch_2_0/embedded/TivaWare/driverlib/ccs/Debug/driverlib.lib" \

-include ../makefile.init

RM := rm -rf
RMDIR := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include subdir_vars.mk
-include Peripherals/subdir_vars.mk
-include subdir_rules.mk
-include Peripherals/subdir_rules.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C55_DEPS)),)
-include $(C55_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
ifneq ($(strip $(S67_DEPS)),)
-include $(S67_DEPS)
endif
ifneq ($(strip $(S62_DEPS)),)
-include $(S62_DEPS)
endif
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(OPT_DEPS)),)
-include $(OPT_DEPS)
endif
ifneq ($(strip $(C??_DEPS)),)
-include $(C??_DEPS)
endif
ifneq ($(strip $(ASM_UPPER_DEPS)),)
-include $(ASM_UPPER_DEPS)
endif
ifneq ($(strip $(S??_DEPS)),)
-include $(S??_DEPS)
endif
ifneq ($(strip $(C64_DEPS)),)
-include $(C64_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(S64_DEPS)),)
-include $(S64_DEPS)
endif
ifneq ($(strip $(INO_DEPS)),)
-include $(INO_DEPS)
endif
ifneq ($(strip $(CLA_DEPS)),)
-include $(CLA_DEPS)
endif
ifneq ($(strip $(S55_DEPS)),)
-include $(S55_DEPS)
endif
ifneq ($(strip $(SV7A_DEPS)),)
-include $(SV7A_DEPS)
endif
ifneq ($(strip $(C62_DEPS)),)
-include $(C62_DEPS)
endif
ifneq ($(strip $(C67_DEPS)),)
-include $(C67_DEPS)
endif
ifneq ($(strip $(PDE_DEPS)),)
-include $(PDE_DEPS)
endif
ifneq ($(strip $(K_DEPS)),)
-include $(K_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(C43_DEPS)),)
-include $(C43_DEPS)
endif
ifneq ($(strip $(S43_DEPS)),)
-include $(S43_DEPS)
endif
ifneq ($(strip $(ASM_DEPS)),)
-include $(ASM_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(SA_DEPS)),)
-include $(SA_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXE_OUTPUTS += \
Stoch_Robot.out \

EXE_OUTPUTS__QUOTED += \
"Stoch_Robot.out" \

BIN_OUTPUTS += \
Stoch_Robot.bin \

BIN_OUTPUTS__QUOTED += \
"Stoch_Robot.bin" \


# All Target
all: $(OBJS) $(CMD_SRCS) $(GEN_CMDS)
	@$(MAKE) --no-print-directory -Onone "Stoch_Robot.out"

# Tool invocations
Stoch_Robot.out: $(OBJS) $(CMD_SRCS) $(GEN_CMDS)
	@echo 'Building target: "$@"'
	@echo 'Invoking: ARM Linker'
	"/home/sashank/ti/ccs901/ccs/tools/compiler/ti-cgt-arm_18.12.1.LTS/bin/armcl" -mv7M4 --code_state=16 --float_support=FPv4SPD16 -me --define=ccs="ccs" --define=PART_TM4C123GH6PM -g --gcc --diag_warning=225 --diag_wrap=off --display_error_number --abi=eabi -z -m"Stoch_Robot.map" --heap_size=0 --stack_size=512 -i"/home/sashank/ti/ccs901/ccs/tools/compiler/ti-cgt-arm_18.12.1.LTS/lib" -i"/home/sashank/ti/ccs901/ccs/tools/compiler/ti-cgt-arm_18.12.1.LTS/include" --reread_libs --diag_wrap=off --display_error_number --warn_sections --xml_link_info="Stoch_Robot_linkInfo.xml" --rom_model -o "Stoch_Robot.out" $(ORDERED_OBJS)
	@echo 'Finished building target: "$@"'
	@echo ' '
	@$(MAKE) --no-print-directory post-build

Stoch_Robot.bin: $(EXE_OUTPUTS)
	@echo 'Building files: $(strip $(EXE_OUTPUTS__QUOTED))'
	@echo 'Invoking: ARM Hex Utility'
	"/home/sashank/ti/ccs901/ccs/tools/compiler/ti-cgt-arm_18.12.1.LTS/bin/armhex"  -o "Stoch_Robot.bin" $(EXE_OUTPUTS__QUOTED)
	@echo 'Finished building: $(strip $(EXE_OUTPUTS__QUOTED))'
	@echo ' '
	@$(MAKE) --no-print-directory post-build

# Other Targets
clean:
	-$(RM) $(BIN_OUTPUTS__QUOTED)$(EXE_OUTPUTS__QUOTED)
	-$(RM) "bezier.obj" "bezier_test.obj" "main.obj" "main2.obj" "tm4c123gh6pm_startup_ccs.obj" "Peripherals/adc.obj" "Peripherals/cpu.obj" "Peripherals/gpio.obj" "Peripherals/interrupt.obj" "Peripherals/pwm.obj" "Peripherals/sysctl.obj" "Peripherals/timer.obj" "Peripherals/uart.obj" "Peripherals/uartstdio.obj" 
	-$(RM) "bezier.d" "bezier_test.d" "main.d" "main2.d" "tm4c123gh6pm_startup_ccs.d" "Peripherals/adc.d" "Peripherals/cpu.d" "Peripherals/gpio.d" "Peripherals/interrupt.d" "Peripherals/pwm.d" "Peripherals/sysctl.d" "Peripherals/timer.d" "Peripherals/uart.d" "Peripherals/uartstdio.d" 
	-@echo 'Finished clean'
	-@echo ' '

post-build:
	-"/home/sashank/ti/ccs901/ccs/utils/tiobj2bin/tiobj2bin" "Stoch_Robot.out" "Stoch_Robot.bin" "/home/sashank/ti/ccs901/ccs/tools/compiler/ti-cgt-arm_18.12.1.LTS/bin/armofd" "/home/sashank/ti/ccs901/ccs/tools/compiler/ti-cgt-arm_18.12.1.LTS/bin/armhex" "/home/sashank/ti/ccs901/ccs/utils/tiobj2bin/mkhex4bin"
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets

