/**
 * Created by yevhenmartynenko on 6/11/17.
 */

document.addEventListener("DOMContentLoaded", function (event) {
    //do work
    var clipboard = new Clipboard('.btn-copy');
    clipboard.on('success', function (e) {
//            console.log(e);
    });
    clipboard.on('error', function (e) {
//            console.log(e);
    });

    document.getElementsByClassName("btn-copy")[0].click(function (e) {
        e.preventDefault();
        var btnHref = this.attr('href');
        var item = this;
        item.text("Copied!");
        item.removeClass('btn-primary');
        item.addClass('btn-success');

        setTimeout(function () {
            item.text("Copy");
            item.removeClass('btn-success');
            item.addClass('btn-primary')
        }, 5000)
    })
});

