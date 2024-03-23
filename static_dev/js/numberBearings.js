function checkBearings() {
    const bearingSelector = document.getElementById('check_bearings').value;
    const bearingSection = document.getElementById('bearings_section');

    if (bearingSelector === 'true') {
        bearingSection.style.display = '';
        countBearing();
    }
    else {
        bearingSection.style.display = 'none';
    }
}

function countBearing(){
    if (document.getElementById('bearings_section').style.display !== 'none') {
        const bearingCount = document.getElementById('bearing_count').value;
        const bearingDiv = document.getElementById('bearings');

        bearingDiv.innerHTML = '';

        for (let i = 0; i < bearingCount; i++) {
            bearingDiv.innerHTML += `
            <hr>
            <fieldset>
                <legend>Rodamiento ${i+1}</legend>
                <div class="form-group mb-3">
                    <label for="side_${i}">Lado del Rodamiento ${i+1}</label>
                    <select class="form-control" name="side_${i}" id="side_${i}" required>
                        <option value="rodamiento delantero">Rodamiento delantero</option>
                        <option value="rodamiento trasero">Rodamiento trasero</option>
                    </select>
                </div>
                <label for="number_reference_${i}">Número de Referencia del Rodamiento ${i+1}</label>
                <input class= 'form-control' type="text" name="number_reference_${i}" id="number_reference_${i}">
            </fieldset>
            `;
        }
    }
}