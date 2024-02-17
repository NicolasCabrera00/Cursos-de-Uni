(function () {

    const btnElimnar = document.querySelectorAll(".btnElimnar");

    btnElimnar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('Seguro de eliminar el curso?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();