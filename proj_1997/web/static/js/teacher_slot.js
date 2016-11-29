$(document).ready(function() {
    $("button.search").click(function() {
        $(".item.ts").show();
        let k = $("input.search").val();
        if(!k.length) {
            return true;
        }
        $(".item.ts").each(function(n, el) {
            if($(el).find("a.header").text().indexOf(k) == -1 && 
                $(el).find("div.description").text().indexOf(k) == -1) {
                $(el).fadeOut();
            }
        });
    });
});