function criarIngrediente() {

   
    var ingrediente = document.getElementById('ingredient_id');
    ingrediente.style.border = '1px solid black'

    if (!ingrediente.value) {
        !ingrediente.value ? ingrediente.style.border = '2px solid red' : null;
        return null;
    }  

    let obj = {name: ingrediente.value}
    var ajax = new XMLHttpRequest();

  
    ajax.open('POST', 'http://127.0.0.1:5000/ingredientes/create', true)
    ajax.setRequestHeader('Content-Type', 'application/json')
    ajax.onload = ((e) => {
        const res = JSON.parse(ajax.responseText)
        if (!res.error) {
            window.location.href = '/ingredientes/create'
        }
        else {
            if (res.error) {
                alert('Erro de cadastro', res)
        }
    } })

    ajax.onerror = (e) => {
        console.error(ajax.statusText);
        }

    ajax.send(JSON.stringify(obj));

    }

