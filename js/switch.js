function Change_theme() {
    if (document.getElementById("switch").checked) {
        console.log("Dark theme");
        // alert('Тёмную тему ещё не завезли')
        let elements = [document.querySelector('html'), document.querySelector('label'), document.getElementById("logo")];
        for (let i of elements) {
            i.style.filter = 'invert()';
        };
        document.querySelector('.bg').style.display = 'none';
    } else {
        console.log("Light theme");
        // alert('Всегда пожалуйста!')
        let elements = [document.querySelector('html'), document.querySelector('label'), document.getElementById("logo")];
        for (let i of elements) {
            i.style.filter = 'none';
        };
        document.querySelector('.bg').style.display = 'block';
    };
}
