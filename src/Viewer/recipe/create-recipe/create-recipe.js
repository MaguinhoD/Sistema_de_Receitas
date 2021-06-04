window.onload = () => {
    IngList = [];
}

function create() {

    const obj = Criarobj()
    
    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/receitas/createrecipe", true);
    ajax.setRequestHeader("Content-type", "application/json");

    ajax.onload = ((e) => {
        var data = JSON.parse(ajax.responseText);
        if (!data.error) {
            window.location.href = '/receitas/criaterecipe'
        }
         else {
            alert(`Tente novamente: ${data.Erro}`)
        }
    })

    ajax.onerror = (e) => {
        console.error(ajax.statusText);
    }

    ajax.send(JSON.stringify(obj));
}


function Addingrediente(){
    var selected = document.getElementById('dropDownIng')
    var qtdselect = document.getElementById('qtd_ingrediente').value
    
    var id = selected.options[selected.selectedIndex].id
    if (!qtdselect) {
        document.getElementById('qtd_ingrediente').style.border = '2px solid red';
        alert('Digite a quantidade')
        return null
    }
    else{
    IngList.push({'id':id})
    
    let lista = document.getElementById('listaing');
    let newList = document.createElement("div");


    newList.innerText = `Ingrediente: ${selected.value} Quantidade: ${qtdselect}` ;   
    lista.append(newList);

    return IngList;}
}



function Criarobj(){

    const ingrediente =  IngList;
        
    
    const name = document.getElementById('recipe_name').value
    if (!name) {
        document.getElementById('recipe_name').style.border = '2px solid red';
        return null
        
    }

    const categoria = document.getElementById('dropDownCat').value;
    if (!categoria) {
        document.getElementById('dropDownCat').style.border = '2px solid red';
        return null
    }

    const steps = document.getElementById('steps').value
    if (!steps) {
        steps.style.border = '2px solid red';
        return null
    }
    return {
        ingrediente,
        name: name,
        category: categoria,
        steps: steps
    }

   }
