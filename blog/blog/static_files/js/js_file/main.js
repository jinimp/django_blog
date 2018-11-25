/*
	Template  Name: Digitalizer Business and Agency HTML Template;
	Template URI: www.bootitems.com
	Description: This is a Business and Agency HTML Template;
	Author: Mushahidul Islam
	Author URI: www.bootitems.com
	Version: 1.0  
*/
/*================================================
[  Table of contents  ]
================================================
	01. jQuery MeanMenu Active
	02. Welcome Slide
	03. Direction Hover Style
	04. Isotope Filter
	05. Project Carousel
	06. Logo Carousel
	07. Testimonial Carousel
	08. Related Project
	09.  CounterUp
	10. Venobox Active
	11. ScrollUp

======================================
[ End table content ]
======================================*/

(function ($) {
 "use strict";

    jQuery(document).ready(function($){
		
		/* ==== 01. jQuery MeanMenu Active ==== */
		if ($('.digitalizer-nav').length) {
			jQuery('.digitalizer-nav').meanmenu();	
		}

		/* ==== 02. Welcome Slide ==== */
		if ($('#welcome-slide').length) {
			$('#welcome-slide').owlCarousel({
				autoplay:false,
				items:1,
				loop:true,
				autoplayHoverPause: false,
				smartSpeed: 500,
				margin:0,
				nav:true,
				navText:['<i class="icofont icofont-arrow-left"></i>','<i class="icofont icofont-arrow-right"></i>'],
				dots:true,
			}) 
		}
		/* ==== 03. Direction Hover Style ==== */
		$(".digitalizer-service-box").snakeify({
		     speed: 300
		   });

		/* ==== 04. Isotope Filter ==== */
		$('.portfolio-wrap').imagesLoaded(function() {
			$('.filter-menu').on('click', 'button', function() {
				var filterValue = $(this).attr('data-filter');
				$grid.isotope({
					filter: filterValue
				});
			});
			var $grid = $('.portfolio-wrap').isotope({
				itemSelector: '.portfolio-item',
				percentPosition: true,
				masonry: {
					columnWidth: '.portfolio-item',
				}
			});
		});
		$('.filter-menu > button').on('click', function(event) {
			$(this).siblings('.active').removeClass('active');
			$(this).addClass('active');
			event.preventDefault();
		});
		/* ==== 05. Project Carousel ==== */
		if ($('.project-wrap').length) {
			$('.project-wrap').owlCarousel({
				autoplay:false,
				items:4,
				loop:true,
				autoplayHoverPause: false,
				smartSpeed: 500,
				margin:10,
				nav:false,
				dots:true,
				responsiveClass:true,
				responsive:{
					0:{
						items:1,
					},
					600:{
						items:2,
					},
					768:{
						items:3,
					},
					1000:{
						items:4,
					}
				}
			}) 
		}

		/* ==== 06. Logo Carousel ==== */
		if ($('.branding-wrap').length) {
			$('.branding-wrap').owlCarousel({
				autoplay:5000,
				loop:true,
				autoplayHoverPause: false,
				smartSpeed: 500,
				nav:false,
				dots:false,
				margin:20,
				responsiveClass:true,
				responsive:{
					0:{
						items:2,
					},
					600:{
						items:3,
					},
					768:{
						items:5,
					},
					1000:{
						items:5,
					}
				}
			}) 
		}

		/* ==== 07. Testimonial Carousel ==== */
		if ($('.testimonial-wrap').length) {
			$('.testimonial-wrap').owlCarousel({
				autoplay:false,
				items:2,
				loop:true,
				autoplayHoverPause: false,
				smartSpeed: 500,
				margin:30,
				nav:false,
				dots:true,
				responsiveClass:true,
				responsive:{
					0:{
						items:1,
					},
					600:{
						items:2,
					},
					768:{
						items:2,
					},
					1000:{
						items:2,
					}
				}
			}) 
		}

		/* ==== 08. Related Project ==== */
		if ($('.related-project-wrap').length) {
			$('.related-project-wrap').owlCarousel({
				autoplay:false,
				items:4,
				loop:true,
				autoplayHoverPause: false,
				smartSpeed: 500,
				margin:30,
				nav:false,
				dots:false,
				responsiveClass:true,
				responsive:{
					0:{
						items:1,
					},
					600:{
						items:2,
					},
					768:{
						items:3,
					},
					1000:{
						items:4,
					}
				}
			}) 
		}
		/* ==== 09. Single Team Member ==== */
		if ($('.other-member-wrap').length) {
			$('.other-member-wrap').owlCarousel({
				autoplay:false,
				items:4,
				loop:true,
				autoplayHoverPause: false,
				smartSpeed: 500,
				margin:30,
				nav:false,
				dots:false,
				responsiveClass:true,
				responsive:{
					0:{
						items:1,
					},
					600:{
						items:2,
					},
					768:{
						items:3,
					},
					1000:{
						items:4,
					}
				}
			}) 
		}

		/* ==== 10. CounterUp ==== */	
		if ($('.counter').length) {
			$('.counter').counterUp({
				delay: 10,
				time: 2000
			});
		}

		/* ==== 11. Venobox Active ==== */	
		if ($('.venobox').length) {
			$('.venobox').venobox(); 
		}

		/* ==== 12. ScrollUp ==== */
		$.scrollUp({
			scrollText: '<i class="icofont-swoosh-up"></i>',
			easingType: 'linear',
			scrollSpeed: 900,
			animation: 'fade'
		}); 
	
    });

	/* ==== 13. Preloader ==== */
	$(window).on('load',function(){
		jQuery(".preloader-wrap").fadeOut(500);
	});
	
})(jQuery); 