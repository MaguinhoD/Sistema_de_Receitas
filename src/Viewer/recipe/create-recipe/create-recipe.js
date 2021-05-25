window.onload = () => {
    Lista=[];
}




function create() {
    let nome = document.getElementById('name');
    let categoria = document.getElementById(('dropDownCat :selected').val());
    let steps = document.getElementById(('steps'));
    

    if (!nome.value || !steps.value) {
        !nome.value ? nome.style.border = '2px solid red' : null;
        !steps.value ? steps.style.border = '2px solid red' : null;
        return null;
    }

    let obj = {'nome': nome.value, 'categoria':categoria.value, 'steps':steps.value, 'Ingredientes':Lista};

    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/createrecipe", true);
    ajax.setRequestHeader("Content-type", "application/json");

    ajax.onload = (e) => {
        var data = JSON.parse(ajax.responseText);
        if (ajax.readyState == 4 && ajax.status == 200) {
            localStorage.setItem('user_id', data.id);
            window.location.href = '/dash/';
        } else {
            alert(`Tente novamente: ${data.Erro}`)
        }
    }

    ajax.onerror = (e) => {
        console.error(ajax.statusText);
    }

    ajax.send(JSON.stringify(obj));
}






function Adicionaringrediente(){

   
    ingrediente =  document.getElementByname(('dropDownIng :selected').name()).id()
    quantidade =  document.getElementByName('qtd_ingrediente').val;
    

    Lista.append('id_ingrediente': idingrediente.value,"quatidade": quantidade.value);

    

   }
