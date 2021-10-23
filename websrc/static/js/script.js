//TODO: Nanti dimodif tergantung kebutuhan, karena jalanin local URL nya jadi belum bisa tes
//function untuk fetch API data -> Belum digunakan, pengganti-nya dari responseallflowss1.js
const fetchAllDataPort = async function () {
    try {
        const response = await fetch("http://192.168.1.106:8080/stats/flow/1");
        const data = await response.json();
        console.log(data);
        return data;
    } catch (err) {
        console.error(err);
    }
};


//menghitung jumlah/banyaknya data berdasarkan port dengan mengambil jumlah terbanyak
function maxCount(data) {
    let inPort1 = 0;
    let inPort2 = 0;
    let inPort3 = 0;

    for (let i = 0; i < data.length; i++) {
        if (data[i].id === 1) {
            inPort1 += 1;
        } else if (data[i].id === 2) {
            inPort2 += 1;
        } else if (data[i].id === 3) {
            inPort3 += 1;
        }
    }

    if (inPort1 > inPort2 && inPort1 > inPort3) {
        return inPort1 + 1;
    } else if (inPort2 > inPort1 && inPort2 > inPort3) {
        return inPort2 + 1;
    } else if (inPort3 > inPort1 && inPort3 > inPort2) {
        return inPort3 + 1;
    }
}

//Jenis Grafik
function typeChart(input) {
    const graph = document.getElementById('Graph');
    graph.innerHTML = `<canvas id="myChart" width="100" height="100"></canvas>`;
    switch(input){
        case "Byte":
            const ctx1 = document.getElementById('myChart');
            const ByteChart = new Chart(ctx1, {
                type: 'line',
                data: {
                    labels: labelX,
                    datasets: [{
                            label: 'in_port1',
                            data: labelAY1,
                            fill: false,
                            borderColor: 'red',
                            borderWidth: 1
                        },
                        {
                            label: 'in_port2',
                            data: labelBY1,
                            fill: false,
                            borderColor: 'green',
                            borderWidth: 1
                        },
                        {
                            label: 'in_port3',
                            data: labelCY1,
                            fill: false,
                            borderColor: 'blue',
                            borderWidth: 1
                        },
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            break;
        case "Packet":
            const ctx2 = document.getElementById('myChart');
            const PacketChart = new Chart(ctx2, {
                type: 'line',
                data: {
                    labels: labelX,
                    datasets: [{
                            label: 'in_port1',
                            data: labelAY2,
                            fill: false,
                            borderColor: 'red',
                            borderWidth: 1
                        },
                        {
                            label: 'in_port2',
                            data: labelBY2,
                            fill: false,
                            borderColor: 'green',
                            borderWidth: 1
                        },
                        {
                            label: 'in_port3',
                            data: labelCY2,
                            fill: false,
                            borderColor: 'blue',
                            borderWidth: 1
                        },
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
            break;
        default:
            const ctxDef = document.getElementById('myChart');
            const def = new Chart(ctxDef, {
                type: 'line',
                data: {
                    labels: labelX,
                    datasets: []
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
            break;
            break;
    }
}


//Mapping data
const dataChart = data[1].map((obj) => ({
    id: obj.match.in_port, //in_port
    packet: obj.packet_count, //packet_count
    byte: obj.byte_count //byte_count
}));

//label X
let labelX = [];
for (let i = 1; i < maxCount(dataChart); i++) {
    labelX.push(i);
}

//label Y Byte
let labelAY1 = [];
let labelBY1 = [];
let labelCY1 = [];
for (let i = 0; i < dataChart.length; i++) {
    if (dataChart[i].id === 1) {
        labelAY1.push(dataChart[i].byte);
    } else if (dataChart[i].id === 2) {
        labelBY1.push(dataChart[i].byte);
    } else if (dataChart[i].id === 3) {
        labelCY1.push(dataChart[i].byte);
    }
}

//label Y Packet Data
let labelAY2 = [];
let labelBY2 = [];
let labelCY2 = [];
for (let i = 0; i < dataChart.length; i++) {
    if (dataChart[i].id === 1) {
        labelAY2.push(dataChart[i].packet);
    } else if (dataChart[i].id === 2) {
        labelBY2.push(dataChart[i].packet);
    } else if (dataChart[i].id === 3) {
        labelCY2.push(dataChart[i].packet);
    }
}


$(document).ready(function () {
    let value = "Byte";
    const inputText = $(`#type_data`);
    inputText.on(`change`, function (e) {
        value = e.target.value;
        typeChart(value);
    })
    typeChart(value);

})