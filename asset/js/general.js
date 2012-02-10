$(document).ready(function() {
	/*
	$(".topmenu .sub-menu .parent a:first").click(function() {
		$(this).parent().children("ul").slideToggle(200);
		$(this).parent().toggleClass("open");
	});
	*/

	$(".sub-menu").parent("li").addClass("parent");
	$(".sub-menu li:first-child").addClass("first");
	$(".sub-menu li:last-child").addClass("last");

	$(".topmenu .sub-menu .parent a").click(function() {
		$(this).parent().children("ul").slideToggle(200);
		$(this).parent().toggleClass("open");
	});
			
	$("ul.tabs").tabs("> .tabcontent", {tabs: 'li'});
	$(".row .col:first-child").addClass("alpha");
	$(".row .col:last-child").addClass("omega"); 
	
// toggle content
	$(".toggle_content").hide(); 
	
	$("h3.toggle").toggle(function(){
		$(this).addClass("active");
		}, function () {
		$(this).removeClass("active");
	});
	
	$("h3.toggle").click(function(){
		$(this).next(".toggle_content").slideToggle();
	});


// pagination
	var islast = $(".pagination .inner a:last").hasClass('page_current');
	if(islast) $(".pagination .inner").css('padding-right','35px');

	if ($.browser.msie  && parseInt($.browser.version) == 7) {
	 	var ispageprev = $(".pagination .inner a").hasClass('page_prev');
		if(ispageprev) $(".pagination, .pagination .inner").css('padding-left','0px');
	}



// gallery
	$(".gl_col_2 .gallery-item::nth-child(2n)").addClass("nomargin");
	$(".gl_col_3 .gallery-item::nth-child(3n)").addClass("nomargin");
	$(".gl_col_4 .gallery-item::nth-child(4n)").addClass("nomargin");
	
	$(".gallery-image a[rel^='prettyPhoto']").prettyPhoto({animationSpeed:'fast'});
		
});

$(function () {  
     $(window).scroll(function () {  
         if ($(this).scrollTop() != 0) {  
             $('.link-top').fadeIn();  
         } else {  
             $('.link-top').fadeOut();  
         }  
     });  
     $('.link-top').click(function () {  
         $('body,html').animate({  
             scrollTop: 0  
         },  
         1500);  
     });  
 });