function getEquipmentCheck() {
    return document.getElementById('equipment_check').value;
}

function checkPumpOrMotor() {
    const equipmentCheck = getEquipmentCheck();
    const equipmentPump = document.getElementById('equipment_pump');
    const equipmentMotor = document.getElementById('equipment_motor');
    const bearingsFields = document.getElementById('bearings');
    const countBearingsSection = document.getElementById('count_bearings');
    const bearingCountSelect = document.getElementById('bearing_count');

    if (equipmentCheck === 'pump') {
        equipmentPump.style.display = '';
        equipmentMotor.style.display = 'none';
        countBearingsSection.style.display = '';
        bearingsFields.innerHTML = '';
    }
    else if (equipmentCheck === 'motor') {
        bearingsFields.innerHTML = '';
        equipmentMotor.style.display = '';
        equipmentPump.style.display = 'none';
        countBearingsSection.style.display = 'none';
        bearingCountSelect.value = "2";
        updateBearingsFields();
    }
    else {
        countBearingsSection.style.display = 'none';
        equipmentMotor.style.display = 'none';
        equipmentPump.style.display = 'none';
        bearingsFields.innerHTML = '';
    }
}

function updateBearingsFields() {
    let equipmentCheck = getEquipmentCheck();
    const bearingsFields = document.getElementById('bearings');
    const bearingCount = document.getElementById('bearing_count').value;

    bearingsFields.innerHTML = '';

    for (let i = 0; i < bearingCount; i++) {
        bearingsFields.innerHTML += `
        <fieldset>
            <legend>Rodamiento ${i+1}</legend>
            <label for="brand_${i}">Fabricante</label>
            <input class= 'form-control' type="text" name="brand_${i}" id="brand_${i}">
            <div class="form-group mb-3">
                <label for="types_${i}">Tipo de Rodamiento</label>
                <select class="form-control" name="types_${i}" id="types_${i}" required>
                    <option value="Rodamiento de bolas rígido">Rodamiento de bolas rígido</option>
                    <option value="Rodamiento de rodillos cilíndricos">Rodamiento de rodillos cilíndricos</option>
                    <option value="Rodamiento de contacto angular de bolas">Rodamiento de contacto angular de bolas</option>
                </select>
            </div>
            <div class="form-group mb-3">
                <label for="side_${i}">Lado del Rodamiento</label>
                <select class="form-control" name="side_${i}" id="side_${i}" required>
                    <option value="rodamiento delantero">Rodamiento delantero</option>
                    <option value="rodamiento trasero">Rodamiento trasero</option>
                </select>
            </div>
            <label for="number_reference_${i}">Número de referencia:</label>
            <input class= 'form-control' type="text" name="number_reference_${i}" id="number_reference_${i}">
            <br>
            <fieldset>
                <legend>Medidas del rodamiento</legend>
                <label for="inner_diameter_${i}">Medida interna (mm):</label>
                <input class= 'form-control' type="number" name="inner_diameter_${i}" id="inner_diameter_${i}">
                <label for="outer_diameter_${i}">Medida externa (mm):</label>
                <input class= 'form-control' type="number" name="outer_diameter_${i}" id="outer_diameter_${i}">
                <label for="broad_${i}">Ancho (mm):</label>
                <input class= 'form-control' type="number" name="broad_${i}" id="broad_${i}">
            </fieldset>
        </fieldset>
        `;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const equipmentCheckElement = document.getElementById('equipment_check');
    const bearingCountElement = document.getElementById('bearing_count');

    if (equipmentCheckElement) {
        equipmentCheckElement.addEventListener('change', checkPumpOrMotor);
    } else {
        console.error('elemento no encontrado.');
    }

    if (bearingCountElement) {
        bearingCountElement.addEventListener('change', updateBearingsFields);
    } else {
        console.error('elemento no encontrado.');
    }
});

