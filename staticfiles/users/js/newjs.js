function tooglelibcontent(id)
{
    $("#panel"+id).toggle();
    if ($("#icon"+id).text() == 'keyboard_arrow_down')
    {
        $("#icon"+id).text('keyboard_arrow_up');
    }
    else
     {
        $("#icon"+id).text('keyboard_arrow_down');
     }
}

function tooglediv(id,panel)
{
    $("#"+id+panel).toggle();
    if ($("#"+panel+id).text() == 'keyboard_arrow_down')
    {
        $("#"+panel+id).text('keyboard_arrow_up');
    }
    else
     {
        $("#"+panel+id).text('keyboard_arrow_down');
     }
}
function toogled(id,panel)
{
    $("#panel"+id).toggle();
    if ($("#"+panel+id).text() == 'arrow_drop_down')
    {
        $("#"+panel+id).text('arrow_drop_up');
    }
    else
     {
        $("#"+panel+id).text('arrow_drop_down');
     }
}
function tooglesearchdiv(icon,panel)
{
    $("#"+panel).toggle();
    if ($("#"+icon).text() == 'keyboard_arrow_down')
    {
        $("#"+icon).text('keyboard_arrow_up');
    }
    else
     {
        $("#"+icon).text('keyboard_arrow_down');
     }
}
