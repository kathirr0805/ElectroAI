projects = {
    "LED Blinking Project": {
        "components": ["LED", "Resistor", "Arduino"],
        "connection": "Components:\n- LED: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino.\n  Connect the LED is shorter leg (cathode, -) to the Arduino is ground (GND) pin via a resistor (typically 220 ohms).\n  The resistor is used to limit the current flowing through the LED and protect it from damage."
    },
    "Temperature Sensor Project": {
        "components": ["LM35 Temperature Sensor", "Arduino", "LCD Display"],
        "connection": "Components:\n- LM35 Temperature Sensor: Connect the LM35 sensor is VCC pin to Arduino is 5V pin.\n  Connect the LM35 sensor is GND pin to Arduino is GND pin.\n  Connect the LM35 sensor is output pin to an analog pin (e.g., A0) on the Arduino.\n- LCD Display: Connect the LCD display to the Arduino for displaying temperature readings."
    },
    "Traffic Light Controller": {
        "components": ["LEDs (Red, Yellow, Green)", "Arduino"],
        "connection": "Components:\n- LEDs (Red, Yellow, Green): Connect each LED to separate digital pins (e.g., pins 2, 3, 4) on the Arduino.\n  Use current-limiting resistors (usually 220 ohms) in series with each LED to prevent excessive current flow.\n- Arduino: Program the Arduino to control the LEDs in a sequence simulating a traffic light."
    },
    "Sound-Activated LED Project": {
        "components": ["Sound Sensor", "LED", "Arduino"],
        "connection": "Components:\n- Sound Sensor: Connect the sound sensor is analog output pin to an analog pin (e.g., A0) on the Arduino.\n- LEDs: Connect the LEDs to digital pins on the Arduino.\n- Arduino: Based on the sound sensor is output, program the Arduino to turn on/off the LEDs."
    },
    "DC Motor Control Project": {
        "components": ["DC Motor", "Motor Driver (L293D)", "Arduino"],
        "connection": "Components:\n- DC Motor: Connect the DC motor to the motor driver is output terminals (OUT1, OUT2 or OUT3, OUT4).\n  Connect the motor driver is input pins (e.g., IN1, IN2) to digital pins on the Arduino.\n- Motor Driver (L293D): Supply power to the motor driver (VCC1, VCC2) and connect the ground (GND) to the Arduino is ground.\n- Arduino: Control the DC motor direction and speed using the motor driver and Arduino."
    }
}
projects.update({
    "infrared remote control": {
        "components": ["infrared sensor", "arduino", "IR LED", "resistor"],
        "connection": "Components:\n- infrared sensor: Connect the sensor is output pin to an analog pin on the Arduino.\n- IR LED: Connect the IR LED is anode to a digital pin on the Arduino and cathode to GND via a resistor.\n- Arduino: Program the Arduino to receive signals from the sensor and control the IR LED for remote control."
    },
    "light intensity meter": {
        "components": ["ldr", "arduino", "LCD display"],
        "connection": "Components:\n- ldr (light-dependent resistor): Connect one leg to 5V, another leg to analog pin on the Arduino, and a resistor to GND.\n- LCD display: Connect the display to the Arduino for showing light intensity readings."
    },
    "auto plant watering system": {
        "components": ["soil moisture sensor", "arduino", "water pump", "transistor"],
        "connection": "Components:\n- soil moisture sensor: Connect the sensor is output to an analog pin on the Arduino.\n- water pump: Connect the pump to a transistor controlled by the Arduino based on moisture levels.\n- Arduino: Program to monitor soil moisture and activate the water pump as needed."
    },
    "motorized blinds control": {
        "components": ["ultrasonic sensor", "arduino", "motor", "motor driver"],
        "connection": "Components:\n- ultrasonic sensor: Connect trigger and echo pins to digital pins on the Arduino.\n- motor driver: Connect to Arduino to control the motor is direction and speed.\n- motor: Connect the motor to the driver.\n- Arduino: Program to detect obstacles and control motorized blinds."
    },
    "heartbeat monitor": {
        "components": ["heartbeat sensor", "arduino", "OLED display"],
        "connection": "Components:\n- heartbeat sensor: Connect to Arduino is analog pin for pulse readings.\n- OLED display: Connect to Arduino for showing real-time heart rate data."
    },
    "automatic pet feeder": {
        "components": ["load cell", "arduino", "servo motor", "H-bridge"],
        "connection": "Components:\n- load cell: Connect to Arduino is analog input to measure food weight.\n- servo motor: Use an H-bridge to control the motor is rotation for food dispensing.\n- Arduino: Program to dispense food based on weight and user settings."
    },
    "gesture-controlled robot": {
        "components": ["accelerometer", "arduino", "robot chassis", "motor driver"],
        "connection": "Components:\n- accelerometer: Connect to Arduino for detecting gestures.\n- motor driver: Control robot motors for movement.\n- Arduino: Program to interpret accelerometer data and control robot movement."
    },
    "smart thermostat": {
        "components": ["temperature sensor", "arduino", "relay module", "LCD display"],
        "connection": "Components:\n- temperature sensor: Connect to Arduino for temperature readings.\n- relay module: Control HVAC systems based on temperature.\n- LCD display: Show temperature and settings."
    },
    "digital alarm clock": {
        "components": ["real-time clock module", "arduino", "buzzer", "LED display"],
        "connection": "Components:\n- real-time clock module: Keep track of time.\n- buzzer: Sound alarm.\n- LED display: Display time and alarms."
    },
    "water level indicator": {
        "components": ["water level sensor", "arduino", "LEDs", "resistor"],
        "connection": "Components:\n- water level sensor: Detect water levels.\n- LEDs: Indicate water level.\n- Arduino: Program to monitor and display water levels."
    },
    "automated door lock system": {
        "components": ["RFID reader", "arduino", "servo motor", "relay module"],
        "connection": "Components:\n- RFID reader: Read RFID tags for access control.\n- servo motor: Lock/unlock door.\n- relay module: Control power to the door lock."
    },
    "WiFi-controlled robot": {
        "components": ["ESP8266 module", "arduino", "robot chassis", "motor driver"],
        "connection": "Components:\n- ESP8266 module: Connect to WiFi network for remote control.\n- motor driver: Control robot motors.\n- Arduino: Program to receive commands over WiFi and control the robot."
    },
    "gas leakage detector": {
        "components": ["gas sensor", "arduino", "buzzer", "LED"],
        "connection": "Components:\n- gas sensor: Detect gas leakage.\n- buzzer and LED: Sound and visual alarm.\n- Arduino: Program to monitor gas levels and trigger alarms."
    },
    "automatic light control": {
        "components": ["PIR sensor", "arduino", "relay module", "LEDs"],
        "connection": "Components:\n- PIR sensor: Detect motion.\n- relay module: Control lights.\n- LEDs: Indicate status."
    },
    "water flow meter": {
        "components": ["flow sensor", "arduino", "LCD display", "sol", "resistor"],
        "connection": "Components:\n- flow sensor: Measure water flow.\n- LCD display: Show flow rate.\n- Arduino: Program to calculate and display flow data."
    },
    "digital voltmeter": {
        "components": ["voltage sensor", "arduino", "LCD display", "resistor"],
        "connection": "Components:\n- voltage sensor: Measure voltage.\n- LCD display: Show voltage readings.\n- Arduino: Program to read and display voltage."
    },
    "voice-controlled light system": {
        "components": ["microphone", "arduino", "relay module", "LEDs"],
        "connection": "Components:\n- microphone: Capture voice commands.\n- relay module: Control lights.\n- LEDs: Indicate status."
    },
    "automated greenhouse system": {
        "components": ["humidity sensor", "arduino", "water pump", "fan", "LEDs"],
        "connection": "Components:\n- humidity sensor: Monitor humidity levels.\n- water pump: Water plants.\n- fan: Control ventilation.\n- LEDs: Indicate system status."
    },
    "smart irrigation system": {
        "components": ["moisture sensor", "arduino", "water valve", "LCD display"],
        "connection": "Components:\n- moisture sensor: Measure soil moisture.\n- water valve: Control water flow.\n- LCD display: Show moisture levels and settings."
    },
    "automatic plant grow light": {
        "components": ["light sensor", "arduino", "LEDs", "relay module"],
        "connection": "Components:\n- light sensor: Measure light levels.\n- LEDs: Provide grow light.\n- relay module: Control light intensity."
    },
    "RFID-based attendance system": {
        "components": ["RFID tags", "arduino", "RFID reader", "LCD display"],
        "connection": "Components:\n- RFID tags: Assign to individuals.\n- RFID reader: Read tags for attendance.\n- LCD display: Show attendance data."
    },
    "solar tracking system": {
        "components": ["light sensor", "arduino", "servo motor", "solar panels"],
        "connection": "Components:\n- light sensor: Detect sunlight.\n- servo motor: Orient solar panels.\n- solar panels: Capture sunlight for energy."
    },
    "Bluetooth-controlled home automation": {
        "components": ["Bluetooth module", "arduino", "relay module", "sensors"],
        "connection": "Components:\n- Bluetooth module: Connect to smartphone for control.\n- relay module: Control home appliances.\n- sensors: Include various sensors for automation."
    }
})
projects.update({
    "automatic pet feeder": {
        "components": ["load cell", "arduino", "servo motor", "H-bridge"],
        "connection": "Components:\n- load cell: Connect to Arduino is analog input to measure food weight.\n- servo motor: Use an H-bridge to control the motor is rotation for food dispensing.\n- Arduino: Program to dispense food based on weight and user settings."
    },
    "gesture-controlled robot": {
        "components": ["accelerometer", "arduino", "robot chassis", "motor driver"],
        "connection": "Components:\n- accelerometer: Connect to Arduino for detecting gestures.\n- motor driver: Control robot motors for movement.\n- Arduino: Program to interpret accelerometer data and control robot movement."
    },
    "smart thermostat": {
        "components": ["temperature sensor", "arduino", "relay module", "LCD display"],
        "connection": "Components:\n- temperature sensor: Connect to Arduino for temperature readings.\n- relay module: Control HVAC systems based on temperature.\n- LCD display: Show temperature and settings."
    },
    "digital alarm clock": {
        "components": ["real-time clock module", "arduino", "buzzer", "LED display"],
        "connection": "Components:\n- real-time clock module: Keep track of time.\n- buzzer: Sound alarm.\n- LED display: Display time and alarms."
    },
    "water level indicator": {
        "components": ["water level sensor", "arduino", "LEDs", "resistor"],
        "connection": "Components:\n- water level sensor: Detect water levels.\n- LEDs: Indicate water level.\n- Arduino: Program to monitor and display water levels."
    },
    "automated door lock system": {
        "components": ["RFID reader", "arduino", "servo motor", "relay module"],
        "connection": "Components:\n- RFID reader: Read RFID tags for access control.\n- servo motor: Lock/unlock door.\n- relay module: Control power to the door lock."
    },
    "WiFi-controlled robot": {
        "components": ["ESP8266 module", "arduino", "robot chassis", "motor driver"],
        "connection": "Components:\n- ESP8266 module: Connect to WiFi network for remote control.\n- motor driver: Control robot motors.\n- Arduino: Program to receive commands over WiFi and control the robot."
    },
    "gas leakage detector": {
        "components": ["gas sensor", "arduino", "buzzer", "LED"],
        "connection": "Components:\n- gas sensor: Detect gas leakage.\n- buzzer and LED: Sound and visual alarm.\n- Arduino: Program to monitor gas levels and trigger alarms."
    },
    "automatic light control": {
        "components": ["PIR sensor", "arduino", "relay module", "LEDs"],
        "connection": "Components:\n- PIR sensor: Detect motion.\n- relay module: Control lights.\n- LEDs: Indicate status."
    },
    "water flow meter": {
        "components": ["flow sensor", "arduino", "LCD display", "sol", "resistor"],
        "connection": "Components:\n- flow sensor: Measure water flow.\n- LCD display: Show flow rate.\n- Arduino: Program to calculate and display flow data."
    },
    "digital voltmeter": {
        "components": ["voltage sensor", "arduino", "LCD display", "resistor"],
        "connection": "Components:\n- voltage sensor: Measure voltage.\n- LCD display: Show voltage readings.\n- Arduino: Program to read and display voltage."
    },
    "voice-controlled light system": {
        "components": ["microphone", "arduino", "relay module", "LEDs"],
        "connection": "Components:\n- microphone: Capture voice commands.\n- relay module: Control lights.\n- LEDs: Indicate status."
    },
    "automated greenhouse system": {
        "components": ["humidity sensor", "arduino", "water pump", "fan", "LEDs"],
        "connection": "Components:\n- humidity sensor: Monitor humidity levels.\n- water pump: Water plants.\n- fan: Control ventilation.\n- LEDs: Indicate system status."
    },
    "smart irrigation system": {
        "components": ["moisture sensor", "arduino", "water valve", "LCD display"],
        "connection": "Components:\n- moisture sensor: Measure soil moisture.\n- water valve: Control water flow.\n- LCD display: Show moisture levels and settings."
    },
    "automatic plant grow light": {
        "components": ["light sensor", "arduino", "LEDs", "relay module"],
        "connection": "Components:\n- light sensor: Measure light levels.\n- LEDs: Provide grow light.\n- relay module: Control light intensity."
    },
    "RFID-based attendance system": {
        "components": ["RFID tags", "arduino", "RFID reader", "LCD display"],
        "connection": "Components:\n- RFID tags: Assign to individuals.\n- RFID reader: Read tags for attendance.\n- LCD display: Show attendance data."
    },
    "solar tracking system": {
        "components": ["light sensor", "arduino", "servo motor", "solar panels"],
        "connection": "Components:\n- light sensor: Detect sunlight.\n- servo motor: Orient solar panels.\n- solar panels: Capture sunlight for energy."
    },
    "Bluetooth-controlled home automation": {
        "components": ["Bluetooth module", "arduino", "relay module", "sensors"],
        "connection": "Components:\n- Bluetooth module: Connect to smartphone for control.\n- relay module: Control home appliances.\n- sensors: Include various sensors for automation."
    },
    "smoke detector system": {
        "components": ["smoke sensor", "arduino", "buzzer", "LED"],
        "connection": "Components:\n- smoke sensor: Detect smoke.\n- buzzer and LED: Sound and visual alarm.\n- Arduino: Program to monitor smoke levels and trigger alarms."
    },
    "automated garage door opener": {
        "components": ["ultrasonic sensor", "arduino", "motor", "motor driver"],
        "connection": "Components:\n- ultrasonic sensor: Detect obstacles.\n- motor driver: Control garage door motor.\n- Arduino: Program to open/close garage door based on sensor inputs."
    },
    "digital tachometer": {
        "components": ["tachometer sensor", "arduino", "LCD display", "resistor"],
        "connection": "Components:\n- tachometer sensor: Measure RPM.\n- LCD display: Show RPM readings.\n- Arduino: Program to read and display RPM."
    },
    "automated fish feeder": {
        "components": ["RTC module", "arduino", "servo motor", "H-bridge"],
        "connection": "Components:\n- RTC module: Keep track of time.\n- servo motor: Use an H-bridge to control the motor is rotation for feeding.\n- Arduino: Program to dispense fish food at scheduled times."
    },
    "IR-based home automation": {
        "components": ["IR receiver", "arduino", "IR transmitter", "relay module"],
        "connection": "Components:\n- IR receiver: Receive IR signals.\n- IR transmitter: Emit IR signals for control.\n- relay module: Control home devices."
    },
    "automated chicken coop door": {
        "components": ["light sensor", "arduino", "servo motor", "RTC module"],
        "connection": "Components:\n- light sensor: Detect daylight.\n- servo motor: Open/close coop door.\n- RTC module: Schedule door operations."
    },
    "automatic water heater controller": {
        "components": ["temperature sensor", "arduino", "relay module", "LCD display"],
        "connection": "Components:\n- temperature sensor: Measure water temperature.\n- relay module: Control water heater.\n- LCD display: Show temperature and settings."
    },
    "smart bin with waste segregation": {
        "components": ["ultrasonic sensor", "arduino", "servo motor", "LEDs"],
        "connection": "Components:\n- ultrasonic sensor: Detect waste levels.\n- servo motor: Control bin flap for segregation.\n- LEDs: Indicate bin status."
    },
    "automated cat feeder": {
        "components": ["weight sensor", "arduino", "servo motor", "RTC module"],
        "connection": "Components:\n- weight sensor: Measure food weight.\n- servo motor: Dispense food.\n- RTC module: Schedule feeding times."
    },
    "automated pet door": {
        "components": ["RFID reader", "arduino", "servo motor", "ultrasonic sensor"],
        "connection": "Components:\n- RFID reader: Identify pets.\n- servo motor: Open/close pet door.\n- ultrasonic sensor: Detect approaching pets."
    },
    "automatic curtain opener": {
        "components": ["light sensor", "arduino", "servo motor", "H-bridge"],
        "connection": "Components:\n- light sensor: Detect daylight.\n- servo motor: Open/close curtains.\n- H-bridge: Control motor direction."
    },
    "Bluetooth-enabled speaker system": {
        "components": ["Bluetooth module", "arduino", "amplifier", "speakers"],
        "connection": "Components:\n- Bluetooth module: Connect to audio source.\n- amplifier: Amplify audio signals.\n- speakers: Output sound."
    },
    "automated plant watering system": {
        "components": ["moisture sensor", "arduino", "water pump", "relay module"],
        "connection": "Components:\n- moisture sensor: Monitor soil moisture.\n- water pump: Water plants.\n- relay module: Control pump based on sensor readings."
    },
    "smart mirror with weather display": {
        "components": ["raspberry pi", "mirror", "LCD display", "weather API"],
        "connection": "Components:\n- raspberry pi: Run the smart mirror software.\n- mirror: Reflect display.\n- LCD display: Show weather information.\n- weather API: Fetch weather data."
    },
    "gesture-controlled lights": {
        "components": ["accelerometer", "arduino", "LED strips", "relay module"],
        "connection": "Components:\n- accelerometer: Detect gestures.\n- LED strips: Control lighting.\n- relay module: Switch lights based on gestures."
    },
    "WiFi-enabled smart doorbell": {
        "components": ["ESP8266 module", "arduino", "camera module", "LCD display"],
        "connection": "Components:\n- ESP8266 module: Connect to WiFi for notifications.\n- camera module: Capture video feed.\n- LCD display: Show doorbell status."
    },
    "home energy monitor": {
        "components": ["energy meter", "arduino", "LCD display", "WiFi module"],
        "connection": "Components:\n- energy meter: Measure electricity usage.\n- LCD display: Show energy consumption.\n- WiFi module: Send data to a monitoring system."
    },
    "automated window blinds": {
        "components": ["light sensor", "arduino", "servo motor", "H-bridge"],
        "connection": "Components:\n- light sensor: Detect sunlight.\n- servo motor: Control blinds.\n- H-bridge: Control motor direction."
    },
    "RFID-based access control system": {
        "components": ["RFID tags", "arduino", "RFID reader", "servo motor"],
        "connection": "Components:\n- RFID tags: Assign to users.\n- RFID reader: Read tags for access.\n- servo motor: Lock/unlock doors."
    },
    "automatic fish tank monitor": {
        "components": ["water level sensor", "arduino", "temperature sensor", "LCD display"],
        "connection": "Components:\n- water level sensor: Monitor water levels.\n- temperature sensor: Measure water temperature.\n- LCD display: Show tank conditions."
    },
    "home weather station": {
        "components": ["weather sensors", "arduino", "LCD display", "WiFi module"],
        "connection": "Components:\n- weather sensors: Measure temperature, humidity, etc.\n- LCD display: Show weather data.\n- WiFi module: Transmit data to online platforms."
    },
    "smart garage door opener": {
        "components": ["ESP8266 module", "arduino", "motor", "motor driver"],
        "connection": "Components:\n- ESP8266 module: Connect to home network.\n- motor driver: Control garage door motor.\n- Arduino: Program to open/close garage door remotely."
    },
    "automated sprinkler system": {
        "components": ["moisture sensor", "arduino", "water valves", "relay module"],
        "connection": "Components:\n- moisture sensor: Detect soil moisture.\n- water valves: Control water flow to different zones.\n- relay module: Trigger valves based on sensor readings."
    },
    "robotic arm controller": {
        "components": ["flex sensors", "arduino", "servo motors", "motor driver"],
        "connection": "Components:\n- flex sensors: Control robotic arm movements.\n- servo motors: Actuate arm joints.\n- motor driver: Interface motors with Arduino."
    },
    "automated medication dispenser": {
        "components": ["RTC module", "arduino", "servo motor", "LCD display"],
        "connection": "Components:\n- RTC module: Schedule medication times.\n- servo motor: Dispense medication doses.\n- LCD display: Show dosage information."
    },
    "smart bicycle light system": {
        "components": ["accelerometer", "arduino", "LEDs", "battery"],
        "connection": "Components:\n- accelerometer: Detect bicycle movements.\n- LEDs: Illuminate based on movement.\n- battery: Power the system."
    },
    "automated greenhouse watering": {
        "components": ["moisture sensor", "arduino", "water pump", "RTC module"],
        "connection": "Components:\n- moisture sensor: Monitor soil moisture.\n- water pump: Irrigate plants.\n- RTC module: Schedule watering times."
    },
    "automated aquarium light": {
        "components": ["light sensor", "arduino", "LED strips", "RTC module"],
        "connection": "Components:\n- light sensor: Detect aquarium light levels.\n- LED strips: Provide lighting.\n- RTC module: Schedule light cycles."
    },
    "robotic vacuum cleaner": {
        "components": ["ultrasonic sensor", "arduino", "motor", "motor driver"],
        "connection": "Components:\n- ultrasonic sensor: Detect obstacles.\n- motor driver: Control vacuum motor.\n- Arduino: Program to navigate and clean."
    },
    "automated plant watering with fertilizer": {
        "components": ["moisture sensor", "arduino", "water pump", "fertilizer pump"],
        "connection": "Components:\n- moisture sensor: Monitor soil moisture.\n- water pump: Provide water.\n- fertilizer pump: Dispense fertilizer.\n- Arduino: Control pumps based on sensor readings."
    },
    "smart home security system": {
        "components": ["PIR sensor", "arduino", "camera module", "alarm system"],
        "connection": "Components:\n- PIR sensor: Detect motion.\n- camera module: Capture video footage.\n- alarm system: Sound alerts."
    },
    "automatic plant lighting": {
        "components": ["light sensor", "arduino", "LEDs", "relay module"],
        "connection": "Components:\n- light sensor: Monitor ambient light.\n- LEDs: Provide artificial light.\n- relay module: Control lighting cycles."
    },
    "smart energy-efficient home": {
        "components": ["energy monitor", "arduino", "relay modules", "sensors"],
        "connection": "Components:\n- energy monitor: Track energy usage.\n- relay modules: Control appliances.\n- sensors: Monitor environmental conditions."
    },
    "automated hydroponics system": {
        "components": ["pH sensor", "arduino", "nutrient pump", "water pump"],
        "connection": "Components:\n- pH sensor: Monitor pH levels.\n- nutrient pump: Dispense nutrients.\n- water pump: Circulate water.\n- Arduino: Control pumps based on sensor readings."
    },
    "smart city traffic management": {
        "components": ["traffic sensors", "arduino", "LED signals", "IoT platform"],
        "connection": "Components:\n- traffic sensors: Monitor traffic flow.\n- LED signals: Control traffic lights.\n- IoT platform: Analyze data and manage traffic."
    },
    "automatic cat litter box": {
        "components": ["weight sensor", "arduino", "servo motor", "scooper"],
        "connection": "Components:\n- weight sensor: Detect litter weight.\n- servo motor: Scoop litter.\n- scooper: Remove waste."
    },
    "automated plant pest control": {
        "components": ["ultrasonic sensor", "arduino", "sprayer", "camera module"],
        "connection": "Components:\n- ultrasonic sensor: Detect pests.\n- sprayer: Apply pest control solutions.\n- camera module: Monitor plant health."
    },
    "smart irrigation with soil analysis": {
        "components": ["moisture sensor", "arduino", "water pump", "Soil pH sensor"],
        "connection": "Components:\n- moisture sensor: Measure soil moisture.\n- water pump: Water plants.\n- Soil pH sensor: Analyze soil acidity."
    },
    "robotic arm with object detection": {
        "components": ["ultrasonic sensor", "arduino", "robotic arm", "motor driver"],
        "connection": "Components:\n- ultrasonic sensor: Detect objects.\n- robotic arm: Manipulate objects.\n- motor driver: Control arm movements."
    },
    "automated garage parking system": {
        "components": ["ultrasonic sensors", "arduino", "servo motors", "LCD display"],
        "connection": "Components:\n- ultrasonic sensors: Detect vehicle positions.\n- servo motors: Control parking mechanism.\n- LCD display: Show parking status."
    },
    "smart trash bin": {
        "components": ["ultrasonic sensor", "arduino", "servo motor", "LEDs"],
        "connection": "Components:\n- ultrasonic sensor: Detect trash levels.\n- servo motor: Open/close bin.\n- LEDs: Indicate bin status."
    },
    "automated greenhouse climate control": {
        "components": ["temperature sensor", "humidity sensor", "arduino", "fans", "heater"],
        "connection": "Components:\n- temperature sensor: Monitor temperature.\n- humidity sensor: Monitor humidity.\n- fans: Control ventilation.\n- heater: Control temperature."
    },
    "smart home lighting system": {
        "components": ["light sensor", "arduino", "LED bulbs", "relay module"],
        "connection": "Components:\n- light sensor: Adjust lighting based on ambient light.\n- LED bulbs: Provide lighting.\n- relay module: Control bulb intensity."
    },
    "automatic pet water dispenser": {
        "components": ["water level sensor", "arduino", "water pump", "relay module"],
        "connection": "Components:\n- water level sensor: Monitor water levels.\n- water pump: Dispense water.\n- relay module: Control pump based on water levels."
    },
    "automated home aquarium": {
        "components": ["water level sensor", "temperature sensor", "arduino", "LED lights"],
        "connection": "Components:\n- water level sensor: Monitor water levels.\n- temperature sensor: Monitor water temperature.\n- LED lights: Control aquarium lighting."
    },
    "smart plant growth monitoring": {
        "components": ["moisture sensor", "light sensor", "temperature sensor", "arduino"],
        "connection": "Components:\n- moisture sensor: Measure soil moisture.\n- light sensor: Monitor light levels.\n- temperature sensor: Monitor temperature.\n- Arduino: Collect and analyze sensor data."
    },
    "automated coffee maker": {
        "components": ["water level sensor", "temperature sensor", "arduino", "heater"],
        "connection": "Components:\n- water level sensor: Monitor water levels.\n- temperature sensor: Monitor water temperature.\n- heater: Heat water for coffee."
    },
    "robotic lawn mower": {
        "components": ["GPS module", "arduino", "lawn mower chassis", "motor driver"],
        "connection": "Components:\n- GPS module: Navigate the mower.\n- motor driver: Control mower motors.\n- Arduino: Program for autonomous mowing."
    },
    "smart parking system": {
        "components": ["ultrasonic sensors", "arduino", "LED indicators", "IoT platform"],
        "connection": "Components:\n- ultrasonic sensors: Detect available parking spaces.\n- LED indicators: Display parking status.\n- IoT platform: Manage parking data."
    },
    "automated cat litter refiller": {
        "components": ["water level sensor", "arduino", "water pump", "LCD display"],
        "connection": "Components:\n- water level sensor: Monitor water levels.\n- water pump: Refill litter.\n- LCD display: Show water level."
    },
    "smart home security camera": {
        "components": ["camera module", "arduino", "WiFi module", "motion sensor"],
        "connection": "Components:\n- camera module: Capture video feed.\n- WiFi module: Connect to home network.\n- motion sensor: Detect movement."
    },
    "automated plant fertilization system": {
        "components": ["moisture sensor", "pH sensor", "arduino", "nutrient pump"],
        "connection": "Components:\n- moisture sensor: Monitor soil moisture.\n- pH sensor: Analyze soil acidity.\n- nutrient pump: Dispense fertilizers."
    },
    "smart mirror with fitness tracker": {
        "components": ["raspberry pi", "mirror", "camera module", "fitness sensors"],
        "connection": "Components:\n- raspberry pi: Run smart mirror software.\n- mirror: Display information.\n- camera module: Capture user data.\n- fitness sensors: Track fitness metrics."
    },
    "automated kitchen garden": {
        "components": ["moisture sensor", "light sensor", "water pump", "arduino"],
        "connection": "Components:\n- moisture sensor: Monitor soil moisture.\n- light sensor: Monitor light levels.\n- water pump: Water plants.\n- Arduino: Automate watering based on sensor readings."
    },
    "smart trash sorting system": {
        "components": ["weight sensor", "color sensor", "arduino", "servo motor"],
        "connection": "Components:\n- weight sensor: Measure trash weight.\n- color sensor: Identify trash type.\n- servo motor: Sort trash bins."
    }
})
projects.update({
    "automatic plant watering with humidity control": {
        "components": ["moisture sensor", "humidity sensor", "arduino", "water pump", "relay module"],
        "connection": "Components:\n- moisture sensor: Monitor soil moisture.\n- humidity sensor: Monitor air humidity.\n- water pump: Water plants.\n- relay module: Control pump based on sensor readings."
    },
    "smart pet feeder": {
        "components": ["weight sensor", "arduino", "servo motor", "LCD display"],
        "connection": "Components:\n- weight sensor: Detect food level.\n- servo motor: Dispense pet food.\n- LCD display: Show feeding schedule."
    },
    "automated greenhouse climate control with CO2 monitoring": {
        "components": ["temperature sensor", "humidity sensor", "CO2 sensor", "arduino", "fans", "heater"],
        "connection": "Components:\n- temperature sensor: Monitor temperature.\n- humidity sensor: Monitor humidity.\n- CO2 sensor: Measure CO2 levels.\n- fans: Control ventilation.\n- heater: Control temperature."
    },
    "smart home energy management system": {
        "components": ["energy monitor", "arduino", "relay modules", "sensors", "WiFi module"],
        "connection": "Components:\n- energy monitor: Track energy usage.\n- relay modules: Control appliances.\n- sensors: Monitor environmental conditions.\n- WiFi module: Connect to a monitoring system."
    },
    "automated hydroponic garden": {
        "components": ["pH sensor", "EC sensor", "arduino", "nutrient pump", "water pump"],
        "connection": "Components:\n- pH sensor: Monitor nutrient acidity.\n- EC sensor: Measure nutrient concentration.\n- nutrient pump: Deliver nutrients.\n- water pump: Circulate water."
    },
    "smart irrigation system with weather prediction": {
        "components": ["moisture sensor", "weather sensors", "arduino", "water pump", "relay module"],
        "connection": "Components:\n- moisture sensor: Monitor soil moisture.\n- weather sensors: Collect weather data.\n- water pump: Irrigate plants.\n- relay module: Control irrigation based on weather predictions."
    },
    "automated vertical farming system": {
        "components": ["LED grow lights", "temperature sensor", "humidity sensor", "arduino", "water pump"],
        "connection": "Components:\n- LED grow lights: Provide light for plants.\n- temperature sensor: Monitor temperature.\n- humidity sensor: Monitor humidity.\n- water pump: Provide water."
    },
    "smart water quality monitoring system": {
        "components": ["pH sensor", "TDS sensor", "temperature sensor", "arduino", "WiFi module"],
        "connection": "Components:\n- pH sensor: Measure water acidity.\n- TDS sensor: Measure total dissolved solids.\n- temperature sensor: Monitor water temperature.\n- WiFi module: Send data to a monitoring platform."
    },
    "automatic pet grooming system": {
        "components": ["brushing module", "shampoo dispenser", "arduino", "servo motor"],
        "connection": "Components:\n- brushing module: Groom pets.\n- shampoo dispenser: Dispense shampoo.\n- servo motor: Control grooming actions."
    },
    "smart health monitoring wearable": {
        "components": ["heart rate sensor", "temperature sensor", "accelerometer", "arduino", "Bluetooth module"],
        "connection": "Components:\n- heart rate sensor: Measure heart rate.\n- temperature sensor: Measure body temperature.\n- accelerometer: Track movement.\n- Bluetooth module: Transmit data to a mobile app."
    },
    "automated home brewery system": {
        "components": ["temperature sensor", "pressure sensor", "arduino", "valves", "pumps"],
        "connection": "Components:\n- temperature sensor: Monitor brewing temperature.\n- pressure sensor: Monitor brewing pressure.\n- valves: Control liquid flow.\n- pumps: Transfer liquids."
    },
    "smart crop monitoring system": {
        "components": ["soil moisture sensor", "temperature sensor", "humidity sensor", "light sensor", "arduino", "WiFi module"],
        "connection": "Components:\n- soil moisture sensor: Monitor soil moisture.\n- temperature sensor: Monitor temperature.\n- humidity sensor: Monitor air humidity.\n- light sensor: Measure light intensity.\n- WiFi module: Send data for analysis."
    },
    "automatic pool cleaning system": {
        "components": ["water level sensor", "pH sensor", "arduino", "pool cleaner", "servo motor"],
        "connection": "Components:\n- water level sensor: Monitor pool water level.\n- pH sensor: Monitor water acidity.\n- pool cleaner: Clean pool surface.\n- servo motor: Control cleaning mechanism."
    },
    "smart classroom attendance system": {
        "components": ["RFID reader", "RFID tags", "arduino", "LCD display"],
        "connection": "Components:\n- RFID reader: Read student tags.\n- RFID tags: Assign to students.\n- LCD display: Show attendance data."
    },
    "automated plant pollination drone": {
        "components": ["drone frame", "propellers", "camera module", "arduino", "pollen dispensers"],
        "connection": "Components:\n- drone frame: Structure for the drone.\n- propellers: Provide lift and thrust.\n- camera module: Guide drone movement.\n- pollen dispensers: Dispense pollen."
    },
    "smart vehicle parking assistance system": {
        "components": ["ultrasonic sensors", "camera module", "arduino", "LCD display", "servo motor"],
        "connection": "Components:\n- ultrasonic sensors: Detect obstacles.\n- camera module: Assist in parking.\n- LCD display: Show parking information.\n- servo motor: Control steering."
    },
    "automatic language translator device": {
        "components": ["microphone", "speaker", "translator module", "arduino"],
        "connection": "Components:\n- microphone: Capture speech.\n- speaker: Output translated speech.\n- translator module: Translate languages.\n- Arduino: Process audio data."
    },
    "smart farm irrigation system": {
        "components": ["soil moisture sensor", "weather sensors", "arduino", "water pumps", "relay module"],
        "connection": "Components:\n- soil moisture sensor: Monitor soil moisture.\n- weather sensors: Collect weather data.\n- water pumps: Irrigate fields.\n- relay module: Control irrigation based on sensor and weather data."
    },
    "automated parcel delivery system": {
        "components": ["RFID tags", "RFID reader", "arduino", "servo motors"],
        "connection": "Components:\n- RFID tags: Attach to parcels.\n- RFID reader: Scan parcel tags.\n- servo motors: Control delivery mechanism."
    },
    "smart home kitchen assistant": {
        "components": ["voice recognition module", "arduino", "robotic arm", "sensors"],
        "connection": "Components:\n- voice recognition module: Recognize commands.\n- robotic arm: Assist in cooking.\n- sensors: Monitor cooking parameters."
    },
    "automatic waste segregation system": {
        "components": ["color sensor", "weight sensor", "arduino", "servo motors"],
        "connection": "Components:\n- color sensor: Identify waste types.\n- weight sensor: Measure waste weight.\n- servo motors: Sort waste bins."
    },
    "smart shopping cart with inventory tracking": {
        "components": ["barcode scanner", "RFID tags", "arduino", "LCD display"],
        "connection": "Components:\n- barcode scanner: Scan products.\n- RFID tags: Track cart contents.\n- LCD display: Show shopping information."
    },
    "automated home brewery with fermentation control": {
        "components": ["temperature sensor", "pH sensor", "arduino", "valves", "pumps", "fermentation chamber"],
        "connection": "Components:\n- temperature sensor: Monitor fermentation temperature.\n- pH sensor: Monitor pH levels.\n- valves: Control liquid flow.\n- pumps: Transfer liquids.\n- fermentation chamber: Control fermentation conditions."
    },
    "smart classroom interactive whiteboard": {
        "components": ["touchscreen display", "camera module", "arduino", "sensors"],
        "connection": "Components:\n- touchscreen display: Interactive board.\n- camera module: Record presentations.\n- sensors: Enhance user interaction."
    },
    "automated rooftop gardening system": {
        "components": ["moisture sensor", "light sensor", "temperature sensor", "arduino", "water pump"],
        "connection": "Components:\n- moisture sensor: Monitor soil moisture.\n- light sensor: Monitor light levels.\n- temperature sensor: Monitor rooftop conditions.\n- water pump: Water plants as needed."
    },
    "smart campus navigation system": {
        "components": ["GPS module", "map data", "arduino", "LED indicators"],
        "connection": "Components:\n- GPS module: Determine location.\n- map data: Provide navigation information.\n- LED indicators: Guide users."
    }
})
projects.update({
    "RC Low-Pass Filter": {
        "components": ["resistor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to the output.\n- Capacitor: Connect one terminal to the output and the other to ground."
    },
    "RC High-Pass Filter": {
        "components": ["resistor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to ground.\n- Capacitor: Connect one terminal to the input and the other to the output."
    },
    "RLC Band-Pass Filter": {
        "components": ["resistor", "inductor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to the output of the circuit.\n- Inductor: Connect one terminal to the output and the other to the input of the circuit.\n- Capacitor: Connect one terminal to ground and the other to the input/output nodes."
    },
    "RLC Notch Filter": {
        "components": ["resistor", "inductor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to the output of the circuit.\n- Inductor: Connect one terminal to the input and the other to ground.\n- Capacitor: Connect one terminal to ground and the other to the output."
    },
    "RC Timer Circuit": {
        "components": ["resistor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to the capacitor.\n- Capacitor: Connect one terminal to ground and the other to the resistor."
    },
    "RLC Oscillator Circuit": {
        "components": ["resistor", "inductor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to the output of the circuit.\n- Inductor: Connect one terminal to ground and the other to the output of the circuit.\n- Capacitor: Connect one terminal to ground and the other to the input of the circuit."
    },
    "RC Integrator Circuit": {
        "components": ["resistor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to the output of the circuit.\n- Capacitor: Connect one terminal to ground and the other to the input of the circuit."
    },
    "RC Differentiator Circuit": {
        "components": ["resistor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to the capacitor.\n- Capacitor: Connect one terminal to ground and the other to the input of the circuit."
    },
    "RLC Filter for Power Supply": {
        "components": ["resistor", "inductor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input voltage and the other to the load.\n- Inductor: Connect one terminal to the load and the other to the output voltage.\n- Capacitor: Connect one terminal to ground and the other to the output voltage."
    },
    "RLC Resonant Circuit": {
        "components": ["resistor", "inductor", "capacitor"],
        "connection": "Components:\n- Resistor: Connect one terminal to the input and the other to the output of the circuit.\n- Inductor: Connect one terminal to the input and the other to the capacitor.\n- Capacitor: Connect one terminal to ground and the other to the inductor."
    }
})
projects.update({
    "led blinking": {
        "components": ["led", "resistor", "arduino"],
        "connection": "Components:\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino.\n  Connect the LED is shorter leg (cathode, -) to the Arduino is ground (gnd) pin via a resistor (typically 220 ohms).\n  The resistor is used to limit the current flowing through the LED and protect it from damage."
    },
    "temperature sensor": {
        "components": ["lm35 temperature sensor", "arduino", "lcd display"],
        "connection": "Components:\n- lm35 temperature sensor: Connect the LM35 sensor is vcc pin to Arduino is 5v pin.\n  Connect the LM35 sensor is gnd pin to Arduino is gnd pin.\n  Connect the LM35 sensor is output pin to an analog pin (e.g., a0) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying temperature readings."
    },
    "traffic light controller": {
        "components": ["leds (red, yellow, green)", "arduino"],
        "connection": "Components:\n- leds (red, yellow, green): Connect each LED to separate digital pins (e.g., pins 2, 3, 4) on the Arduino.\n  Use current-limiting resistors (usually 220 ohms) in series with each LED to prevent excessive current flow.\n- arduino: Program the Arduino to control the LEDs in a sequence simulating a traffic light."
    },
    "sound-activated led project": {
        "components": ["sound sensor", "leds", "arduino"],
        "connection": "Components:\n- sound sensor: Connect the sound sensor is analog output pin to an analog pin (e.g., a0) on the Arduino.\n- leds: Connect the LEDs to digital pins on the Arduino.\n- arduino: Based on the sound sensor is output, program the Arduino to turn on/off the LEDs."
    },
    "dc motor control project": {
        "components": ["dc motor", "motor driver (l293d)", "arduino"],
        "connection": "Components:\n- dc motor: Connect the DC motor to the motor driver is output terminals (out1, out2 or out3, out4).\n  Connect the motor driver is input pins (e.g., in1, in2) to digital pins on the Arduino.\n- motor driver (l293d): Supply power to the motor driver (vcc1, vcc2) and connect the ground (gnd) to the Arduino is ground.\n- arduino: Control the DC motor direction and speed using the motor driver and Arduino."
    },
    "arduino buzzer project": {
        "components": ["buzzer", "arduino"],
        "connection": "Components:\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino.\n  Connect the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to generate tones and control the buzzer."
    },
    "arduino button project": {
        "components": ["push button", "arduino", "led"],
        "connection": "Components:\n- push button: Connect one leg of the button to a digital pin (e.g., pin 2) on the Arduino and the other leg to the ground (gnd) pin.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to turn on the LED when the button is pressed."
    },
    "arduino potentiometer project": {
        "components": ["potentiometer", "arduino", "led"],
        "connection": "Components:\n- potentiometer: Connect one end of the potentiometer to 5v, the other end to ground (gnd), and the wiper (middle pin) to an analog pin (e.g., a0) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 9) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to vary the LED brightness based on the potentiometer is position."
    },
    "arduino servo motor project": {
        "components": ["servo motor", "arduino", "potentiometer"],
        "connection": "Components:\n- servo motor: Connect the servo motor is signal wire to a digital pin (e.g., pin 9) on the Arduino.\n  Connect the servo motor is power (vcc) and ground (gnd) wires to the Arduino is 5v and ground pins, respectively.\n- arduino: Program the Arduino to control the servo motor is position based on input from the potentiometer."
    },
    "arduino temperature and humidity sensor project": {
        "components": ["dht11 sensor", "arduino", "lcd display"],
        "connection": "Components:\n- dht11 sensor: Connect the sensor is vcc pin to Arduino is 5v pin.\n  Connect the sensor is gnd pin to Arduino is gnd pin.\n  Connect the sensor is data pin to a digital pin (e.g., pin 2) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying temperature and humidity readings."
    },
    "arduino light sensor project": {
        "components": ["light-dependent resistor (ldr)", "arduino", "led"],
        "connection": "Components:\n- ldr: Connect one leg of the LDR to the analog pin (e.g., a0) on the Arduino and the other leg to 5v.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to adjust LED brightness based on LDR readings."
    },
    "arduino ultrasonic sensor project": {
        "components": ["ultrasonic sensor (hc-sr04)", "arduino", "led"],
        "connection": "Components:\n- ultrasonic sensor: Connect the sensor is vcc pin to Arduino is 5v pin.\n  Connect the sensor is gnd pin to Arduino is gnd pin.\n  Connect the sensor is trig and echo pins to digital pins (e.g., trig to pin 9 and echo to pin 10) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to measure distance using the ultrasonic sensor and control the LED based on distance thresholds."
    },
    "arduino pir motion sensor project": {
        "components": ["pir motion sensor", "arduino", "led"],
        "connection": "Components:\n- pir motion sensor: Connect the sensor is vcc pin to Arduino is 5v pin.\n  Connect the sensor is gnd pin to Arduino is gnd pin.\n  Connect the sensor is output pin to a digital pin (e.g., pin 2) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect motion using the PIR sensor and control the LED accordingly."
    },
    "arduino tilt sensor project": {
        "components": ["tilt sensor", "arduino", "led"],
        "connection": "Components:\n- tilt sensor: Connect one terminal of the tilt sensor to a digital pin (e.g., pin 2) on the Arduino and the other terminal to the ground (gnd) pin.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect tilting using the sensor and illuminate the LED."
    },
    "arduino flame sensor project": {
        "components": ["flame sensor", "arduino", "led"],
        "connection": "Components:\n- flame sensor: Connect the sensor is vcc pin to Arduino is 5v pin.\n  Connect the sensor is gnd pin to Arduino is gnd pin.\n  Connect the sensor is output pin to a digital pin (e.g., pin 2) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect flames using the sensor and activate the LED when flames are detected."
    },
    "arduino ldr and servo motor project": {
        "components": ["light-dependent resistor (ldr)", "arduino", "servo motor"],
        "connection": "Components:\n- ldr: Connect one leg of the LDR to the analog pin (e.g., a0) on the Arduino and the other leg to 5v.\n- servo motor: Connect the servo motor is signal wire to a digital pin (e.g., pin 9) on the Arduino.\n  Connect the servo motor is power (vcc) and ground (gnd) wires to the Arduino is 5v and ground pins, respectively.\n- arduino: Program the Arduino to move the servo motor based on LDR readings."
    },
    "arduino rgb led project": {
        "components": ["rgb led", "arduino"],
        "connection": "Components:\n- rgb led: Connect the longer legs of the RGB LED (common cathode) to digital pins (e.g., pins 9, 10, 11) on the Arduino.\n  Connect the shorter leg (common anode) to a current-limiting resistor and then to the ground (gnd) pin.\n- arduino: Program the Arduino to control the RGB LED is colors by adjusting the PWM signals on the respective pins."
    },
    "arduino relay module project": {
        "components": ["relay module", "arduino", "led"],
        "connection": "Components:\n- relay module: Connect the relay module is vcc to Arduino is 5v pin, gnd to gnd pin, and in1 (or control pin) to a digital pin (e.g., pin 2) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to the relay module is com (common) pin and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to control the relay module, which in turn controls the LED."
    }
})
projects.update({
    "arduino sound sensor project": {
        "components": ["sound sensor", "arduino", "led"],
        "connection": "Components:\n- sound sensor: Connect the sound sensor is analog output pin to an analog pin (e.g., a0) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to respond to sound levels detected by the sensor."
    },
    "arduino ir remote control project": {
        "components": ["ir receiver module", "arduino", "ir remote"],
        "connection": "Components:\n- ir receiver module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 11) on the Arduino.\n- ir remote: Use the IR remote to send commands to the receiver module.\n- arduino: Program the Arduino to interpret IR signals from the remote and perform corresponding actions."
    },
    "arduino lcd display project": {
        "components": ["lcd display", "arduino", "potentiometer"],
        "connection": "Components:\n- lcd display: Connect the LCD display is vcc to Arduino is 5v pin, gnd to gnd pin, scl to a digital pin (e.g., pin 13), and sda to another digital pin (e.g., pin 12) on the Arduino.\n- potentiometer: Connect one end of the potentiometer to 5v, the other end to ground (gnd), and the wiper (middle pin) to the LCD display is v0 pin for contrast adjustment.\n- arduino: Program the Arduino to display text or data on the LCD."
    },
    "arduino temperature control project": {
        "components": ["lm35 temperature sensor", "arduino", "relay module"],
        "connection": "Components:\n- lm35 temperature sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and output pin to an analog pin (e.g., a0) on the Arduino.\n- relay module: Connect the relay module is vcc to Arduino is 5v pin, gnd to gnd pin, and in1 (or control pin) to a digital pin (e.g., pin 2) on the Arduino.\n- arduino: Program the Arduino to read temperature data and control a device (e.g., fan, heater) using the relay based on temperature thresholds."
    },
    "arduino motor speed control project": {
        "components": ["dc motor", "arduino", "motor driver (l298n)", "potentiometer"],
        "connection": "Components:\n- dc motor: Connect the DC motor to the motor driver is output terminals (out1, out2 or out3, out4).\n  Connect the motor driver is input pins (e.g., in1, in2) to digital pins on the Arduino.\n- motor driver (l298n): Supply power to the motor driver (vcc1, vcc2) and connect the ground (gnd) to the Arduino is ground.\n- potentiometer: Connect one end of the potentiometer to 5v, the other end to ground (gnd), and the wiper (middle pin) to an analog pin (e.g., a0) on the Arduino.\n- arduino: Program the Arduino to control the speed of the motor using the potentiometer."
    },
    "arduino keypad entry project": {
        "components": ["4x4 keypad", "arduino", "lcd display"],
        "connection": "Components:\n- 4x4 keypad: Connect the keypad is rows and columns to digital pins on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying keypad inputs.\n- arduino: Program the Arduino to detect and display keypad entries on the LCD."
    },
    "arduino digital thermometer project": {
        "components": ["ds18b20 temperature sensor", "arduino", "lcd display"],
        "connection": "Components:\n- ds18b20 temperature sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 2) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying temperature readings.\n- arduino: Program the Arduino to read and display temperature data from the sensor."
    },
    "arduino proximity sensor project": {
        "components": ["ir proximity sensor", "arduino", "led"],
        "connection": "Components:\n- ir proximity sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 9) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect nearby objects using the proximity sensor and control the LED."
    },
    "arduino water level sensor project": {
        "components": ["water level sensor", "arduino", "led"],
        "connection": "Components:\n- water level sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 7) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect water levels using the sensor and illuminate the LED based on the water level."
    },
    "arduino ultrasonic distance meter project": {
        "components": ["hc-sr04 ultrasonic sensor", "arduino", "lcd display"],
        "connection": "Components:\n- hc-sr04 ultrasonic sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, echo pin to a digital pin (e.g., pin 11), and trigger pin to another digital pin (e.g., pin 12) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying distance measurements.\n- arduino: Program the Arduino to measure and display distance using the ultrasonic sensor."
    },
    "arduino accelerometer project": {
        "components": ["accelerometer sensor", "arduino", "led"],
        "connection": "Components:\n- accelerometer sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and x, y, z output pins to analog pins (e.g., a0, a1, a2) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to read accelerometer data and control the LED based on movements."
    },
    "arduino soil moisture sensor project": {
        "components": ["soil moisture sensor", "arduino", "led"],
        "connection": "Components:\n- soil moisture sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 5) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to monitor soil moisture levels using the sensor and activate the LED accordingly."
    },
    "arduino flame detection project": {
        "components": ["flame sensor", "arduino", "led"],
        "connection": "Components:\n- flame sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 3) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect flames using the sensor and activate the LED when flames are detected."
    },
    "arduino distance measurement project": {
        "components": ["infrared distance sensor", "arduino", "lcd display"],
        "connection": "Components:\n- infrared distance sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, out pin to a digital pin (e.g., pin 4), and gnd2 to gnd pin on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying distance measurements.\n- arduino: Program the Arduino to measure and display distance using the infrared sensor."
    },
    "arduino light following robot project": {
        "components": ["light-dependent resistor (ldr)", "arduino", "dc motors", "motor driver (l293d)"],
        "connection": "Components:\n- ldr: Connect one leg of the LDR to an analog pin (e.g., a0) on the Arduino and the other leg to 5v.\n- dc motors: Connect the motors to the motor driver is output terminals (out1, out2 or out3, out4).\n  Connect the motor driver is input pins (e.g., in1, in2) to digital pins on the Arduino.\n- motor driver (l293d): Supply power to the motor driver (vcc1, vcc2) and connect the ground (gnd) to the Arduino is ground.\n- arduino: Program the Arduino to control the robot is movement based on LDR readings."
    },
    "arduino gas sensor project": {
        "components": ["gas sensor", "arduino", "led"],
        "connection": "Components:\n- gas sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 6) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect gas levels using the sensor and activate the LED based on gas concentration."
    },
    "arduino color sensing project": {
        "components": ["tcs3200 color sensor", "arduino", "led"],
        "connection": "Components:\n- tcs3200 color sensor: Connect the sensor is s0, s1, s2, s3, out pins to digital pins on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect and differentiate colors using the color sensor and control the LED based on color detection."
    },
    "arduino pulse rate monitoring project": {
        "components": ["heart rate sensor", "arduino", "lcd display"],
        "connection": "Components:\n- heart rate sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, sda to a digital pin (e.g., pin 2), and scl to another digital pin (e.g., pin 3) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying pulse rate readings.\n- arduino: Program the Arduino to monitor and display pulse rate using the sensor."
    },
    "arduino touch sensor project": {
        "components": ["capacitive touch sensor", "arduino", "led"],
        "connection": "Components:\n- capacitive touch sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 4) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect touch using the sensor and control the LED."
    },
    "arduino tilt alarm project": {
        "components": ["tilt sensor", "arduino", "buzzer"],
        "connection": "Components:\n- tilt sensor: Connect one terminal of the tilt sensor to a digital pin (e.g., pin 2) on the Arduino and the other terminal to the ground (gnd) pin.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to sound an alarm when tilt is detected."
    },
    "arduino humidity control project": {
        "components": ["dht11 humidity sensor", "arduino", "humidity fan"],
        "connection": "Components:\n- dht11 humidity sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 2) on the Arduino.\n- humidity fan: Connect the fan to a relay module controlled by the Arduino.\n- arduino: Program the Arduino to monitor humidity levels using the sensor and control the fan based on humidity thresholds."
    },
    "arduino water flow sensor project": {
        "components": ["water flow sensor", "arduino", "lcd display"],
        "connection": "Components:\n- water flow sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 5) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying water flow readings.\n- arduino: Program the Arduino to monitor and display water flow using the sensor."
    },
    "arduino co2 sensor project": {
        "components": ["co2 sensor", "arduino", "lcd display"],
        "connection": "Components:\n- co2 sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 2) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying co2 concentration readings.\n- arduino: Program the Arduino to detect and display co2 levels using the sensor."
    },
    "arduino flame alarm project": {
        "components": ["flame sensor", "arduino", "buzzer"],
        "connection": "Components:\n- flame sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 3) on the Arduino.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to sound an alarm when flames are detected by the sensor."
    },
    "arduino smoke detector project": {
        "components": ["smoke sensor", "arduino", "led"],
        "connection": "Components:\n- smoke sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 3) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect smoke using the sensor and activate the LED when smoke is detected."
    },
    "arduino humidity display project": {
        "components": ["dht22 humidity sensor", "arduino", "lcd display"],
        "connection": "Components:\n- dht22 humidity sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 2) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying humidity readings.\n- arduino: Program the Arduino to read and display humidity data from the sensor."
    },
    "arduino vibration sensor project": {
        "components": ["vibration sensor", "arduino", "led"],
        "connection": "Components:\n- vibration sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 2) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect vibrations using the sensor and control the LED."
    }
})
projects.update({
    "arduino rain sensor project": {
        "components": ["rain sensor", "arduino", "buzzer"],
        "connection": "Components:\n- rain sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 4) on the Arduino.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to sound an alarm when rain is detected by the sensor."
    },
    "arduino magnetic door alarm project": {
        "components": ["reed switch", "arduino", "buzzer"],
        "connection": "Components:\n- reed switch: Connect one terminal of the reed switch to a digital pin (e.g., pin 2) on the Arduino and the other terminal to the ground (gnd) pin.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to sound an alarm when the door is opened (reed switch triggered)."
    },
    "arduino light dimmer project": {
        "components": ["light dimmer module", "arduino", "ac bulb"],
        "connection": "Components:\n- light dimmer module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and signal pin to a digital pin (e.g., pin 6) on the Arduino.\n- ac bulb: Connect the bulb to the light dimmer module for dimming control.\n- arduino: Program the Arduino to control the brightness of the AC bulb using the light dimmer module."
    },
    "arduino bluetooth controlled robot project": {
        "components": ["bluetooth module (hc-05)", "arduino", "dc motors"],
        "connection": "Components:\n- bluetooth module (hc-05): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- dc motors: Connect the motors to motor driver outputs controlled by the Arduino.\n- arduino: Program the Arduino to receive commands via Bluetooth and control the robot is movements."
    },
    "arduino gas leakage detector project": {
        "components": ["gas sensor", "arduino", "buzzer"],
        "connection": "Components:\n- gas sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 7) on the Arduino.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to sound an alarm when gas leakage is detected by the sensor."
    },
    "arduino motorized blinds project": {
        "components": ["servo motor", "arduino", "ir remote"],
        "connection": "Components:\n- servo motor: Connect the motor to a digital pin (e.g., pin 9) on the Arduino.\n- ir remote: Use the IR remote to send commands for controlling the blinds.\n- arduino: Program the Arduino to receive IR signals from the remote and adjust the servo motor for opening/closing the blinds."
    },
    "arduino water level indicator project": {
        "components": ["water level sensor", "arduino", "led"],
        "connection": "Components:\n- water level sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 4) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to indicate water levels using the sensor and LED."
    },
    "arduino auto intensity street light project": {
        "components": ["ldr", "arduino", "relay module", "ac street light"],
        "connection": "Components:\n- ldr: Connect one leg of the LDR to an analog pin (e.g., a0) on the Arduino and the other leg to 5v.\n- relay module: Connect the relay module is vcc to Arduino is 5v pin, gnd to gnd pin, and in1 (or control pin) to a digital pin (e.g., pin 2) on the Arduino.\n- ac street light: Connect the street light to the relay module for automatic intensity control.\n- arduino: Program the Arduino to control street light intensity based on ambient light detected by the LDR."
    },
    "arduino humidity and temperature monitor project": {
        "components": ["dht11 humidity and temperature sensor", "arduino", "lcd display"],
        "connection": "Components:\n- dht11 sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 3) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying humidity and temperature readings.\n- arduino: Program the Arduino to read and display humidity and temperature data from the sensor."
    },
    "arduino automatic plant watering system project": {
        "components": ["moisture sensor", "arduino", "water pump", "relay module"],
        "connection": "Components:\n- moisture sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 6) on the Arduino.\n- water pump: Connect the pump to a relay module controlled by the Arduino.\n- relay module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and in1 (or control pin) to a digital pin (e.g., pin 7) on the Arduino.\n- arduino: Program the Arduino to water plants based on soil moisture readings from the sensor."
    },
    "arduino automated greenhouse project": {
        "components": ["temperature sensor", "humidity sensor", "arduino", "fan", "heater"],
        "connection": "Components:\n- temperature sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 3) on the Arduino.\n- humidity sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to another digital pin (e.g., pin 4) on the Arduino.\n- fan: Connect the fan to a relay module controlled by the Arduino.\n- heater: Connect the heater to another relay module controlled by the Arduino.\n- arduino: Program the Arduino to maintain optimal conditions in a greenhouse by controlling fan and heater based on temperature and humidity."
    },
    "arduino wifi temperature monitor project": {
        "components": ["wifi module (esp8266)", "temperature sensor", "arduino", "lcd display"],
        "connection": "Components:\n- wifi module (esp8266): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to Arduino is rx pin, and rx to Arduino is tx pin.\n- temperature sensor: Connect the sensor is vcc to Arduino is 3.3v pin (if compatible), gnd to gnd pin, and data pin to a digital pin (e.g., pin 2) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying temperature readings.\n- arduino: Program the Arduino to read temperature data from the sensor and send it over WiFi using the ESP8266 module."
    },
    "arduino automatic door opening system project": {
        "components": ["pir motion sensor", "servo motor", "arduino"],
        "connection": "Components:\n- pir motion sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 2) on the Arduino.\n- servo motor: Connect the motor to a digital pin (e.g., pin 9) on the Arduino.\n- arduino: Program the Arduino to detect motion using the PIR sensor and automatically open the door using the servo motor."
    },
    "arduino bluetooth music player project": {
        "components": ["bluetooth module (hc-05)", "arduino", "speaker"],
        "connection": "Components:\n- bluetooth module (hc-05): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- speaker: Connect the speaker to the Arduino for audio output.\n- arduino: Program the Arduino to receive music data via Bluetooth and play it through the speaker."
    },
    "arduino ultrasonic parking system project": {
        "components": ["ultrasonic sensor", "arduino", "lcd display", "buzzer"],
        "connection": "Components:\n- ultrasonic sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, trig to a digital pin (e.g., pin 4), and echo to another digital pin (e.g., pin 5) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying parking distance.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to measure parking distance using the ultrasonic sensor and display it on the LCD while sounding an alarm when close to obstacles."
    },
    "arduino gesture controlled robot project": {
        "components": ["accelerometer sensor", "arduino", "dc motors"],
        "connection": "Components:\n- accelerometer sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, sda to a digital pin (e.g., pin a4), and scl to another digital pin (e.g., pin a5) on the Arduino.\n- dc motors: Connect the motors to motor driver outputs controlled by the Arduino.\n- arduino: Program the Arduino to interpret gesture data from the accelerometer and control the robot is movements."
    },
    "arduino rfid based security system project": {
        "components": ["rfid reader", "arduino", "lcd display", "buzzer"],
        "connection": "Components:\n- rfid reader: Connect the reader is vcc to Arduino is 5v pin, gnd to gnd pin, rx to a digital pin (e.g., pin 2), and tx to another digital pin (e.g., pin 3) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying security status.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to read RFID tags and grant access based on valid tags while alerting with the buzzer."
    },
    "arduino automatic pet feeder project": {
        "components": ["servo motor", "arduino", "rtc module", "lcd display"],
        "connection": "Components:\n- servo motor: Connect the motor to a digital pin (e.g., pin 9) on the Arduino.\n- rtc module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, sda to a digital pin (e.g., pin a4), and scl to another digital pin (e.g., pin a5) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying feeding schedule.\n- arduino: Program the Arduino to dispense pet food at scheduled times using the servo motor and RTC module."
    },
    "arduino bluetooth door lock project": {
        "components": ["bluetooth module (hc-05)", "arduino", "servo motor"],
        "connection": "Components:\n- bluetooth module (hc-05): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- servo motor: Connect the motor to a digital pin (e.g., pin 9) on the Arduino.\n- arduino: Program the Arduino to unlock/lock a door using Bluetooth commands to control the servo motor."
    },
    "arduino gps tracking system project": {
        "components": ["gps module", "arduino", "lcd display"],
        "connection": "Components:\n- gps module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying GPS coordinates.\n- arduino: Program the Arduino to receive GPS data and display the current location on the LCD."
    },
    "arduino alcohol detector project": {
        "components": ["alcohol sensor", "arduino", "lcd display", "buzzer"],
        "connection": "Components:\n- alcohol sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 7) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying alcohol levels.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to detect alcohol levels using the sensor and alert with the buzzer."
    },
    "arduino tilt sensor project": {
        "components": ["tilt sensor", "arduino", "led"],
        "connection": "Components:\n- tilt sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 2) on the Arduino.\n- led: Connect the LED is longer leg (anode, +) to a digital pin (e.g., pin 13) on the Arduino and the shorter leg (cathode, -) to a current-limiting resistor connected to ground (gnd).\n- arduino: Program the Arduino to detect tilting using the sensor and control the LED."
    },
    "arduino voice controlled home automation project": {
        "components": ["voice recognition module", "arduino", "relay modules", "lights", "fans"],
        "connection": "Components:\n- voice recognition module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- relay modules: Connect the modules to the Arduino for controlling lights, fans, etc.\n- arduino: Program the Arduino to recognize voice commands and trigger relay modules for home automation."
    },
    "arduino temperature controlled fan project": {
        "components": ["temperature sensor", "arduino", "fan"],
        "connection": "Components:\n- temperature sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 2) on the Arduino.\n- fan: Connect the fan to a relay module controlled by the Arduino.\n- arduino: Program the Arduino to monitor temperature using the sensor and control the fan speed based on temperature thresholds."
    },
    "arduino smart irrigation system project": {
        "components": ["soil moisture sensor", "arduino", "water pump", "relay module"],
        "connection": "Components:\n- soil moisture sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 6) on the Arduino.\n- water pump: Connect the pump to a relay module controlled by the Arduino.\n- relay module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and in1 (or control pin) to a digital pin (e.g., pin 7) on the Arduino.\n- arduino: Program the Arduino to water plants based on soil moisture readings from the sensor."
    },
    "arduino color sorting machine project": {
        "components": ["color sensor", "arduino", "servo motor", "conveyor belt"],
        "connection": "Components:\n- color sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, sda to a digital pin (e.g., pin a4), and scl to another digital pin (e.g., pin a5) on the Arduino.\n- servo motor: Connect the motor to control the sorting mechanism.\n- conveyor belt: Connect the belt motor to a motor driver controlled by the Arduino.\n- arduino: Program the Arduino to detect and sort objects based on color using the color sensor and servo motor."
    },
    "arduino automatic pet door project": {
        "components": ["rfid reader", "arduino", "servo motor"],
        "connection": "Components:\n- rfid reader: Connect the reader is vcc to Arduino is 5v pin, gnd to gnd pin, rx to a digital pin (e.g., pin 2), and tx to another digital pin (e.g., pin 3) on the Arduino.\n- servo motor: Connect the motor to a digital pin (e.g., pin 9) on the Arduino.\n- arduino: Program the Arduino to open/close a pet door based on recognized RFID tags using the servo motor."
    }
})
projects.update({
    "arduino wireless weather station project": {
        "components": ["dht22 sensor", "arduino", "wifi module (esp8266)", "lcd display"],
        "connection": "Components:\n- dht22 sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 3) on the Arduino.\n- wifi module (esp8266): Connect the module is vcc to Arduino is 3.3v pin, gnd to gnd pin, tx to Arduino is rx pin, and rx to Arduino is tx pin.\n- lcd display: Connect the LCD display to the Arduino for displaying weather data.\n- arduino: Program the Arduino to read weather data from the sensor and send it over WiFi using the ESP8266 module."
    },
    "arduino voice-controlled car project": {
        "components": ["voice recognition module", "arduino", "motor driver (l298n)", "dc motors"],
        "connection": "Components:\n- voice recognition module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- motor driver (l298n): Connect the driver is input pins to Arduino is digital pins for controlling motor direction and speed.\n- dc motors: Connect the motors to the motor driver outputs.\n- arduino: Program the Arduino to receive voice commands and control the car is movements."
    },
    "arduino wifi controlled led matrix project": {
        "components": ["led matrix", "arduino", "wifi module (esp8266)"],
        "connection": "Components:\n- led matrix: Connect the matrix is data pins to Arduino is digital pins for controlling LED patterns.\n- wifi module (esp8266): Connect the module is vcc to Arduino is 3.3v pin, gnd to gnd pin, tx to Arduino is rx pin, and rx to Arduino is tx pin.\n- arduino: Program the Arduino to receive LED display commands over WiFi and control the LED matrix."
    },
    "arduino laser security system project": {
        "components": ["laser module", "ldr sensor", "arduino", "buzzer"],
        "connection": "Components:\n- laser module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and signal pin to a digital pin (e.g., pin 4) on the Arduino.\n- ldr sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to another digital pin (e.g., pin 5) on the Arduino.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to detect interruptions in the laser beam using the LDR sensor and sound an alarm with the buzzer."
    },
    "arduino bluetooth-controlled home lighting project": {
        "components": ["bluetooth module (hc-05)", "arduino", "relay modules", "led bulbs"],
        "connection": "Components:\n- bluetooth module (hc-05): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- relay modules: Connect the modules to the Arduino for controlling LED bulbs.\n- led bulbs: Connect the bulbs to the relay modules.\n- arduino: Program the Arduino to receive lighting commands via Bluetooth and control the LED bulbs."
    },
    "arduino wifi doorbell project": {
        "components": ["push button", "arduino", "wifi module (esp8266)", "buzzer"],
        "connection": "Components:\n- push button: Connect one terminal of the button to a digital pin (e.g., pin 2) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for input.\n- wifi module (esp8266): Connect the module is vcc to Arduino is 3.3v pin, gnd to gnd pin, tx to Arduino is rx pin, and rx to Arduino is tx pin.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to detect button presses and trigger a doorbell sound over WiFi using the ESP8266 module."
    },
    "arduino obstacle avoiding robot project": {
        "components": ["ultrasonic sensor", "arduino", "dc motors", "motor driver (l293d)"],
        "connection": "Components:\n- ultrasonic sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, trig to a digital pin (e.g., pin 4), and echo to another digital pin (e.g., pin 5) on the Arduino.\n- dc motors: Connect the motors to motor driver outputs controlled by the Arduino.\n- motor driver (l293d): Connect the driver is input pins to Arduino is digital pins for motor control.\n- arduino: Program the Arduino to detect obstacles using the ultrasonic sensor and maneuver the robot to avoid them."
    },
    "arduino gesture-controlled lamp project": {
        "components": ["accelerometer sensor", "arduino", "led lamp"],
        "connection": "Components:\n- accelerometer sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, sda to a digital pin (e.g., pin a4), and scl to another digital pin (e.g., pin a5) on the Arduino.\n- led lamp: Connect the lamp to a digital pin (e.g., pin 9) on the Arduino.\n- arduino: Program the Arduino to interpret gesture data from the accelerometer and control the lamp is brightness or on/off state."
    },
    "arduino wifi-controlled robot arm project": {
        "components": ["robot arm", "arduino", "wifi module (esp8266)", "servo motors"],
        "connection": "Components:\n- robot arm: Connect the arm is servo motors to digital pins on the Arduino for control.\n- wifi module (esp8266): Connect the module is vcc to Arduino is 3.3v pin, gnd to gnd pin, tx to Arduino is rx pin, and rx to Arduino is tx pin.\n- arduino: Program the Arduino to receive commands over WiFi and control the robot arm is movements."
    },
    "arduino smart garden watering system project": {
        "components": ["soil moisture sensor", "arduino", "water pump", "relay module"],
        "connection": "Components:\n- soil moisture sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 6) on the Arduino.\n- water pump: Connect the pump to a relay module controlled by the Arduino.\n- relay module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and in1 (or control pin) to a digital pin (e.g., pin 7) on the Arduino.\n- arduino: Program the Arduino to water plants based on soil moisture readings from the sensor."
    },
    "arduino temperature-controlled fan with lcd display project": {
        "components": ["temperature sensor", "arduino", "lcd display", "fan"],
        "connection": "Components:\n- temperature sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 2) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying temperature readings.\n- fan: Connect the fan to a relay module controlled by the Arduino.\n- arduino: Program the Arduino to monitor temperature using the sensor and control the fan speed based on temperature readings shown on the LCD."
    },
    "arduino bluetooth-controlled robot car project": {
        "components": ["bluetooth module (hc-05)", "arduino", "motor driver (l298n)", "dc motors"],
        "connection": "Components:\n- bluetooth module (hc-05): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- motor driver (l298n): Connect the driver is input pins to Arduino is digital pins for controlling motor direction and speed.\n- dc motors: Connect the motors to the motor driver outputs.\n- arduino: Program the Arduino to receive Bluetooth commands and control the robot car is movements."
    },
    "arduino smoke detector alarm project": {
        "components": ["smoke sensor", "arduino", "buzzer"],
        "connection": "Components:\n- smoke sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and out pin to a digital pin (e.g., pin 7) on the Arduino.\n- buzzer: Connect one terminal of the buzzer to a digital pin (e.g., pin 8) on the Arduino and the other terminal to either the ground (gnd) pin or another digital pin for tone control.\n- arduino: Program the Arduino to detect smoke using the sensor and sound an alarm with the buzzer."
    },
    "arduino wifi-controlled robotic arm project": {
        "components": ["robotic arm", "arduino", "wifi module (esp8266)", "servo motors"],
        "connection": "Components:\n- robotic arm: Connect the arm is servo motors to digital pins on the Arduino for control.\n- wifi module (esp8266): Connect the module is vcc to Arduino is 3.3v pin, gnd to gnd pin, tx to Arduino is rx pin, and rx to Arduino is tx pin.\n- arduino: Program the Arduino to receive commands over WiFi and control the robotic arm is movements."
    },
    "arduino bluetooth-controlled robotic car project": {
        "components": ["bluetooth module (hc-05)", "arduino", "motor driver (l298n)", "dc motors"],
        "connection": "Components:\n- bluetooth module (hc-05): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- motor driver (l298n): Connect the driver is input pins to Arduino is digital pins for controlling motor direction and speed.\n- dc motors: Connect the motors to the motor driver outputs.\n- arduino: Program the Arduino to receive Bluetooth commands and control the robotic car is movements."
    },
    "arduino automatic plant watering system project": {
        "components": ["moisture sensor", "arduino", "water pump", "relay module"],
        "connection": "Components:\n- moisture sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and analog pin to an analog pin (e.g., A0) on the Arduino.\n- water pump: Connect the pump to a relay module controlled by the Arduino.\n- relay module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and in1 (or control pin) to a digital pin (e.g., pin 7) on the Arduino.\n- arduino: Program the Arduino to water plants based on soil moisture readings from the sensor."
    },
    "arduino bluetooth-controlled robotic arm project": {
        "components": ["bluetooth module (hc-05)", "arduino", "servo motors"],
        "connection": "Components:\n- bluetooth module (hc-05): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- servo motors: Connect the motors to digital pins on the Arduino for control.\n- arduino: Program the Arduino to receive Bluetooth commands and control the robotic arm is movements."
    },
    "arduino temperature and humidity monitoring system project": {
        "components": ["dht11 sensor", "arduino", "lcd display"],
        "connection": "Components:\n- dht11 sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and data pin to a digital pin (e.g., pin 3) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying temperature and humidity readings.\n- arduino: Program the Arduino to read temperature and humidity data from the sensor and display it on the LCD."
    },
    "arduino color-changing lamp project": {
        "components": ["rgb led", "arduino"],
        "connection": "Components:\n- rgb led: Connect the LED is red, green, and blue pins to digital pins on the Arduino for color control.\n- arduino: Program the Arduino to change the color of the RGB LED based on user input or predefined patterns."
    },
    "arduino gps tracker project": {
        "components": ["gps module", "arduino", "gsm module", "battery"],
        "connection": "Components:\n- gps module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 4), and rx to another digital pin (e.g., pin 5) on the Arduino.\n- gsm module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 6), and rx to another digital pin (e.g., pin 7) on the Arduino.\n- battery: Power the Arduino and modules using a battery.\n- arduino: Program the Arduino to track GPS location data and send it via GSM for remote tracking."
    },
    "arduino smartwatch project": {
        "components": ["oled display", "arduino", "bluetooth module (hc-05)"],
        "connection": "Components:\n- oled display: Connect the display is vcc to Arduino is 5v pin, gnd to gnd pin, sda to a digital pin (e.g., pin a4), and scl to another digital pin (e.g., pin a5) on the Arduino.\n- bluetooth module (hc-05): Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, tx to a digital pin (e.g., pin 2), and rx to another digital pin (e.g., pin 3) on the Arduino.\n- arduino: Program the Arduino to display smartwatch functions and receive/control data over Bluetooth."
    },
    "arduino digital clock project": {
        "components": ["real-time clock (rtc) module", "arduino", "lcd display"],
        "connection": "Components:\n- real-time clock (rtc) module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, sda to a digital pin (e.g., pin a4), and scl to another digital pin (e.g., pin a5) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying time.\n- arduino: Program the Arduino to read time from the RTC module and display it on the LCD as a digital clock."
    },
    "arduino digital thermometer project": {
        "components": ["lm35 temperature sensor", "arduino", "lcd display"],
        "connection": "Components:\n- lm35 temperature sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and output pin to an analog pin (e.g., A0) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying temperature readings.\n- arduino: Program the Arduino to read temperature data from the sensor and display it on the LCD as a digital thermometer."
    },
    "arduino pwm-controlled led dimmer project": {
        "components": ["potentiometer", "arduino", "led"],
        "connection": "Components:\n- potentiometer: Connect one terminal of the potentiometer to Arduino is 5v pin, the other terminal to gnd pin, and the center pin (wiper) to an analog pin (e.g., A0) on the Arduino.\n- led: Connect the LED to a digital pin (e.g., pin 9) on the Arduino for dimming control.\n- arduino: Program the Arduino to read potentiometer values and adjust the LED brightness using PWM (Pulse Width Modulation)."
    },
    "arduino automatic light intensity controller project": {
        "components": ["ldr sensor", "arduino", "led"],
        "connection": "Components:\n- ldr sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and output pin to an analog pin (e.g., A0) on the Arduino.\n- led: Connect the LED to a digital pin (e.g., pin 9) on the Arduino for brightness control.\n- arduino: Program the Arduino to read light intensity from the sensor and adjust the LED brightness accordingly."
    },
    "arduino ir remote-controlled car project": {
        "components": ["ir receiver module", "arduino", "motor driver (l298n)", "dc motors"],
        "connection": "Components:\n- ir receiver module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and signal pin to a digital pin (e.g., pin 2) on the Arduino.\n- motor driver (l298n): Connect the driver is input pins to Arduino is digital pins for controlling motor direction and speed.\n- dc motors: Connect the motors to the motor driver outputs.\n- arduino: Program the Arduino to receive IR remote commands and control the car is movements."
    },
    "arduino pid-controlled temperature system project": {
        "components": ["lm35 temperature sensor", "arduino", "heater (resistor)", "fan"],
        "connection": "Components:\n- lm35 temperature sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and output pin to an analog pin (e.g., A0) on the Arduino.\n- heater (resistor): Connect the heater to a relay module controlled by the Arduino.\n- fan: Connect the fan to another relay module controlled by the Arduino.\n- arduino: Program the Arduino to implement PID (Proportional-Integral-Derivative) control for maintaining a set temperature, controlling the heater and fan accordingly."
    },
    "arduino automatic street light controller project": {
        "components": ["ldr sensor", "arduino", "relay module", "street lights"],
        "connection": "Components:\n- ldr sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and output pin to an analog pin (e.g., A0) on the Arduino.\n- relay module: Connect the module is vcc to Arduino is 5v pin, gnd to gnd pin, and in1 (or control pin) to a digital pin (e.g., pin 7) on the Arduino.\n- street lights: Connect the lights to the relay module controlled by the Arduino.\n- arduino: Program the Arduino to control street lights based on ambient light levels detected by the sensor."
    },
    "arduino heart rate monitoring system project": {
        "components": ["heart rate sensor", "arduino", "lcd display"],
        "connection": "Components:\n- heart rate sensor: Connect the sensor is vcc to Arduino is 5v pin, gnd to gnd pin, and output pin to an analog pin (e.g., A0) on the Arduino.\n- lcd display: Connect the LCD display to the Arduino for displaying heart rate readings.\n- arduino: Program the Arduino to read heart rate data from the sensor and display it on the LCD."
    }
})

