function addTask(){
    const div = document.getElementById('new-task-div')
    div.innerHTML = '<textarea name="list_content" class="textarea-content center-block"></textarea><button type="submit" form="new-task-form" class="btn btn-dark margin-btm-10px text-outline center-block">Add</button>';

}


function deleteTask(){
    alert("Task successfully deleted!");
}

const delAll = document.getElementById('hide-btn');

function deleteAllPrompt(){
    if (confirm("Are you sure?") == true) {
        delAll.click();
        alert("You've deleted all tasks!");
    }
}


function editTask(id){
    const div = document.getElementById(`edit-task-${id}`)
    let content = document.getElementById('task-content').textContent
    div.innerHTML = `<textarea name="new-task-content" class="edit-div center-block">${content}</textarea><button type="submit" class="btn btn-dark margin-btm-10px text-outline center-block">Save</button>`;
}