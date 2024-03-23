function pageOrigin(origin){
    localStorage.setItem('pageOriginForm', origin);
}

document.addEventListener('DOMContentLoaded', function() {
    let linkPump = document.getElementsByClassName('linkPump');
    for (let link of linkPump) {
        console.log('pump1')
        link.addEventListener('click', () => {
            pageOrigin('pump');
        });
    }

    let linkBearing = document.getElementById('linkBearing');
    if (linkBearing) {
        linkBearing.addEventListener('click', () => {
            pageOrigin('bearing');
        });
    }
    const origin = localStorage.getItem('pageOriginForm');
    if (origin === 'bearing') {
        let equipmentChecks = document.getElementById('check');
            if (equipmentChecks) {
                equipmentChecks.style.display = '';
            }
    }

    let returnButton = document.getElementById('returnButton');
    if (returnButton) {
        returnButton.addEventListener('click', redirectAccordingOrigin);
    }
});

function redirectAccordingOrigin() {
    const origin = localStorage.getItem('pageOriginForm');

    switch (origin) {
        case 'pump':
            console.log('pump')
            window.location.href = '/pumps/';
            break;
        case 'bearing':
            window.location.href = '/bearings/bearings/';
            break;
        default:
            break;
    }
    equipmentCheck = document.getElementById('equipment_check');
    localStorage.removeItem('pageOriginForm');
}
