addMessage('ElectroAI: Good Morning','');
addMessage('ElectroAI: I am Electro AI. How may I assist you today?','');
document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    addMessage('User:', userInput); // Add "User:" prefix
    document.getElementById('user-input').value = "";

    setTimeout(() => {
        const botReply = getBotResponse(userInput);
        addMessage('ElectroAI:', botReply); // Add "Electro AI:" prefix
    }, 1000);
}

function addMessage(sender, text) {
    const chatBody = document.getElementById('chat-body');
    const message = document.createElement('div');
    message.classList.add('chat-message');
    message.innerHTML = `<strong>${sender}</strong> ${text}`; // Display sender before the message
    chatBody.appendChild(message);
    chatBody.scrollTop = chatBody.scrollHeight;
}

function getBotResponse(input) {
    const responses = {
        'resistor': 'A resistor is a passive two-terminal electronic component that resists the flow of electric current. It is used to control the amount of current in a circuit, voltage division, and as a load.',
        'capacitor': 'A capacitor is a passive two-terminal electronic component that stores electrical energy in an electric field. It is used for filtering, energy storage, coupling, and timing applications.',
        'inductor': 'An inductor is a passive electronic component that stores energy in a magnetic field when current flows through it. It is used in filtering, energy storage, and impedance matching.',
        'diode': 'A diode is a semiconductor device that allows current to flow in one direction only. It is used in rectification, signal demodulation, and voltage regulation.',
        'transistor': 'A transistor is a semiconductor device used to amplify or switch electronic signals and electrical power. It is fundamental in digital and analog circuits, amplifiers, and switching applications.',
        'operational amplifier': 'An operational amplifier is a high-gain electronic voltage amplifier with differential inputs. It is used in amplification, filtering, signal conditioning, and mathematical operations.',
        'MOSFET': 'A MOSFET is a type of field-effect transistor used for switching and amplifying electronic signals. It is widely used in power electronics, digital circuits, and high-frequency applications.',
        'voltage regulator': 'A voltage regulator is an electronic circuit that maintains a constant output voltage irrespective of changes in input voltage or load conditions. It is used for power supply stabilization and voltage control.',
        'integrated circuit': 'An integrated circuit is a miniaturized electronic circuit consisting of semiconductor devices and passive components on a single chip. It is used in nearly all electronic devices for functions such as processing, memory, and control.',
        'microcontroller': 'A microcontroller is a small computer on a single integrated circuit containing a processor core, memory, and programmable input/output peripherals. It is used in embedded systems, IoT devices, and control applications.',
        'crystal oscillator': 'A crystal oscillator is an electronic circuit that uses the mechanical resonance of a vibrating crystal to create an electrical signal with precise frequency. It is used in timing, clock generation, and synchronization.',
        'LED': 'A light-emitting diode is a semiconductor light source that emits light when current flows through it. It is used for indicator lights, displays, illumination, and optical communication.',
        'LCD': 'A liquid crystal display is a flat-panel display technology that uses liquid crystals to produce visual information. It is used in electronic devices such as monitors, TVs, and digital screens.',
        'potentiometer': 'A potentiometer is a variable resistor with three terminals used to adjust the voltage or resistance in a circuit. It is used for volume controls, tuning, and analog input adjustments.',
        'relay': 'A relay is an electrically operated switch that uses an electromagnet to mechanically control the switching of a circuit. It is used for switching high-power loads, motor control, and automation.',
        'sensor': 'A sensor is a device that detects and responds to a physical stimulus, converting it into an electrical signal. Sensors are used in measurement, monitoring, control systems, and IoT applications.',
        'battery': 'A battery is a device that stores chemical energy and converts it into electrical energy. Batteries are used as power sources in electronic devices, portable equipment, and energy storage systems.',
        'switch': 'A switch is a mechanical or electronic device used to interrupt or divert the flow of electric current in a circuit. Switches are used for control, on/off operations, and circuit routing.',
        'fuse': 'A fuse is a safety device used to protect electrical circuits from overcurrent and short circuits. Fuses are designed to break the circuit when the current exceeds a predetermined threshold.',
        'resistor array': 'A resistor array or network is a package of multiple resistors in a single integrated circuit. It is used for precision resistance matching, voltage division, and compact circuit.',
        'project helper': 'Sure, I can help you with project ideas based on the components you have. Please list the components you have.',
        'resistor capacitor':'RC Low-Pass Filter: Components: Connect one terminal of Resistor to the input and the other to the output.Connect one terminal of Capacitor to the output and the other to ground.',
    };
    return responses[input.toLowerCase()] || "I'm sorry, I don't understand that.";
}

