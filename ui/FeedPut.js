function new_plan()
{
    console.log("Added New plan button detected!");
    var plan = document.getElementById('modal1');
    var instance = M.Modal.getInstance(plan);
    instance.open();
}
