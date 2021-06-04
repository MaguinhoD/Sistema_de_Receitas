function deleteObj(id) {
    if (!id) {
        return null
    }

    let ajax = new XMLHttpRequest()
    ajax.open('DELETE', `http://localhost:5000/ingredientes/delete/${id}`, true)
    ajax.setRequestHeader('Content-Type', 'application/json')

    ajax.onload = (() => {
        const res = JSON.parse(ajax.responseText)
        console.log(res)
        if (!res.error) {
            document.getElementById(`ingredient_${id}`).remove()
            window.location.href = '/ingredientes'
        } else {
            alert('Ingrediente vinculado a uma receita, não é possivel deleta-lo')
        }
    })

    ajax.onerror = (error => {
        console.log('ajax error:', error)
    })

    ajax.send(undefined)
    
}