$(document).ready(function() {
    let search_rsv = function() {
        // $("tr.teacher").show();
        let k = $("input.search").val();
        // console.log(k);
        if(!k.length) {
            return true;
        }
        $("tr.rsv").each(function(n, el) {
            if($(el).find("td.name").text().indexOf(k) == -1 && 
                $(el).find("td.slots").text().indexOf(k) == -1 && 
                $(el).find("td.other").text().indexOf(k) == -1) {
                $(el).fadeOut("fast");
            } else {
                $(el).fadeIn();
            }
        });
    }

    $("button.search").click(search_rsv);
    $("input.search").keyup(search_rsv);

    $("table.sortable").tablesort();
});