

function sendRegister() {
    

    var name = document.getElementById('name');
    var email = document.getElementById('email');
    var email2 = document.getElementById('email2');
    var password =  document.getElementById('password');
    var password2  = document.getElementById('password2');

    if (!email.value || !password.value || !name.value || !email2.value || !password2.value) { // ! inverso, se for null
        !email.value ? email.style.border = '2px solid red' : null; //if tenario
        !email2.value ? email2.style.border = '2px solid red' : null;
        !password.value ? password.style.border = '2px solid red' : null;
        !password2.value ? password2.style.border = '2px solid red' : null;
        !name.value ? name.style.border = '2px solid red' : null;
        
        return null;
    }  

    let obj = { 
        name: name.value,
        email: email.value,
        password: password.value
    }

    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/account/registerUser", true);
    ajax.setRequestHeader("Content-type", "application/json");

    ajax.onload = (e) => {
        var data = JSON.parse(ajax.responseText);
        if (email.value==email2.value){
            if (password.value==password2.value){
                if (ajax.readyState == 4 && ajax.status == 200) {   // State 4 = operação concluida, status 200 = OK
                    localStorage.setItem('user_id', data.id);
                    window.location.href = '/dash/';
                } 
                else {
                     alert(`Tente novamente: ${data.Erro}`)
                }
            }
            else {alert('Senhas diferentes')}
    }
        else {
            alert('Email diferentes')
    }
    }

    ajax.onerror = (e) => {
        console.error(ajax.statusText);
    }

    ajax.send(JSON.stringify(obj));

}