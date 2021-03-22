function logout() {
    localStorage.removeItem('user_id')
    window.location.href = '/';
}
function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }

  function openForm2() {
    document.getElementById("myForm2").style.display = "block";
  }
  
  function closeForm2() {
    document.getElementById("myForm2").style.display = "none";
  }

function sendLogin() {
    let email = document.getElementById('email');
    let senha = document.getElementById('password');

    if (!email.value || !senha.value) {
        !email.value ? email.style.border = '2px solid red' : null;
        !senha.value ? senha.style.border = '2px solid red' : null;
        return null;
    }

    let obj = {'email': email.value, 'password':senha.value}

    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/getUser", true);
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

document.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        sendLogin()
    }
});

function sendRegister() {
    

   
    var email = document.getElementById('emailr');
    var password =  document.getElementById('pswr');
    var password2  = document.getElementById('pswr2');

      let obj = { 
        
        email: email.value,
        password: password.value
    }

    var ajax = new XMLHttpRequest();

    // Pega o tipo de requisição: Post e a URL da API
    ajax.open("POST", "http://127.0.0.1:5000/account/registerUser", true);
    ajax.setRequestHeader("Content-type", "application/json");

    ajax.onload = (e) => {
        var data = JSON.parse(ajax.responseText);
        
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
       
    
    

    ajax.onerror = (e) => {
        console.error(ajax.statusText);
    }

    ajax.send(JSON.stringify(obj));

}