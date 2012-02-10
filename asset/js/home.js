function load_animations(){
		
			if (!$.browser.msie) {
				$('#header_images').css({height: '468px', opacity:'0'})
				$('#aside2').css({height:'558px', opacity:'0'});
				$('#overlay_bg').css({height:'468px'});
							
				$('#header_controls_left').animate({opacity:'1'});
				$('#header_controls_right').animate({opacity:'1'});
				
				$('#header_images').stop().animate({opacity:'1'},400,'easeOutQuad');
				$('#header_images > .header_image:first-child').stop().animate({opacity: '1'},400,'easeOutQuad');
				$('#aside2').stop().animate({opacity:'1'},400,'easeOutQuad');
				
			}
			else{
				$('#header_images').css({height: '468px'});
				$('#aside2').css({height:'558px'});
				$('#overlay_bg').css({height:'468px'});
				$('#header_images .header_image').stop().animate({opacity:'0'},0);
				$('#header_images .header_image:first-child').stop().animate({opacity:'1'},0);
			}
    
		/// end animation in ///		
		var header_count = $("#header_images > .header_image").size();
		var current_project = 1;
 		var header_color = $('.header_image').attr('color');		
 		     	
     	$('#aside2').css({'background-image':'none','background-color':header_color});
     	 
		
		$('#overlay_bg')
		.click(function(event){
		window.location=($('#header_images > img:nth-child('+current_project+')').attr('link'));
		});
		$('#aside2')
		.hover(
		function(event){
		$('#header_controls_left').show();
		$('#header_controls_right').show();
		if (!$.browser.msie) {
			$('#header_controls_left').stop().animate({left:'0px'},200,'easeOutQuad');
			$('#header_controls_right').stop().animate({right:'0px'},200,'easeOutQuad');
		}},
		function(event){
		$('#header_controls_left').hide();
		$('#header_controls_right').hide();
		if (!$.browser.msie) {
			$('#header_controls_left').stop().animate({left:'10px'},300,'easeOutQuad');
			$('#header_controls_right').stop().animate({right:'10px'},300,'easeOutQuad');
		}})
		
		$('#header_controls_right').click(function(event){animate_header('right',0);clearInterval(interval_header);})
		
		$('#header_controls_left').click(function(event){animate_header('left',0);clearInterval(interval_header);})
		
		document.onkeyup = handleArrowKeys;
		
		function handleArrowKeys(evt) {
		if (evt.keyCode == 37){animate_header('left',0);clearInterval(interval_header);}
		if (evt.keyCode == 39){animate_header('right',0);clearInterval(interval_header);}
		}
		
		
		function animate_header(direction,project){
		if (!$.browser.msie) {
			$('#header_images > .header_image:nth-child('+current_project+')').stop().animate({opacity:'0',marginLeft:'-100px',marginTop:'-50px',width:'1210px',height:'590px'},250,'easeInQuad', function(){
			$(this).css({marginLeft:'0px',marginTop:'0px',width:'960px',height:'468px'})			

			
						
			if(direction == 'logo'){current_project = project};
			if(direction == 'left'){current_project--};
			if(direction == 'right'){current_project++};
			if(current_project>header_count){current_project=1};
			if(current_project<1){current_project=header_count};
			
			
			var new_color = $('#header_images > .header_image:nth-child('+current_project+')').attr('color')
			//$('#aside2').animate({backgroundColor:new_color},80,'easeOutQuart');
			$('#aside2').css({backgroundColor: new_color});
			$('#header_images > .header_image:nth-child('+current_project+')').css({marginLeft:'100px',marginTop:'50px',width:'760px',height:'340px'});
			$('#header_images > .header_image:nth-child('+current_project+')').stop().animate({opacity: '1',marginLeft:'0',marginTop:'0',width:'960px',height:'468px'},250,'easeOutQuad');
			});
		}
		else{
			$('#header_images > .header_image:nth-child('+current_project+')').stop().animate({opacity:'0'},150,'easeInQuad', function(){

			if(direction == 'logo'){current_project = project};
			if(direction == 'left'){current_project--};
			if(direction == 'right'){current_project++};
			if(current_project>header_count){current_project=1};
			if(current_project<1){current_project=header_count};
			
			var new_color = $('#header_images > .header_image:nth-child('+current_project+')').attr('color')
			//$('#aside2').animate({backgroundColor: new_color},80,'easeOutQuart');
			$('#aside2').css({backgroundColor: new_color});
			$('#header_images > .header_image:nth-child('+current_project+')').stop().animate({opacity: '1'},150,'easeInQuad');
			});
		}
		}

		var interval_header = setInterval(timerFunction, 4000);
		
		function timerFunction(){
		animate_header('right',0);
		}
}