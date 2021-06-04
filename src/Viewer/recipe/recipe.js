function deleteObj(id) {
    if (!id) {
        return null
    }

    let ajax = new XMLHttpRequest()
    ajax.open('DELETE', `http://localhost:5000/receitas/delete/${id}`, true)
    ajax.setRequestHeader('Content-Type', 'application/json')

    ajax.onload = (() => {
        const res = JSON.parse(ajax.responseText)
        console.log(res)
        if (!res.error) {
            document.getElementById(`recipe_${id}`).remove()
            window.location.href = '/receitas'
        } else {
            alert('Não possivel deletar')
        }
    })

    ajax.onerror = (error => {
        console.log('ajax error:', error)
    })

    ajax.send(undefined)
    
}