import re

html='''<div class="p-img">
			<a target="_blank" title="维多利亚旅行者 VICTORIATOURIST 双肩包电脑包15.6英寸 男商务防水双肩背包V9006灰色" href="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80MTU4ODEyLmh0bWw&log=89D2X8fH443l26lO_iBKNtU5A-4B-y9_kHAIaZc5bhGQ_bwwcAmL5l1hFfXjwQEDw5exHLdLXHsIKwslHK-Ais9w2TJ2EO4o5FlCyuUDUVQ8nVgkGqiKKPcLJaAxiGVqwEYEwhHoLcKkOQlxAm7DUBDEP8r4BP66NAuW2e9mpEQH12ioHZjk3UTrJ_5XIjYr9qKBaG9LDpyQPKOLbZUL9gGPfAciW-j0UyFdQKf5bJv8FunD9TGwtEreXt2q7__0Vg4tVIFVc8mXZ8U9xiXEIUo7ijr-Iq3PgqcbqFD6p5Ec80W_TBuZA5lMHclKoQJFvb6yQFvM-GkKX5oaAs35a6T3Fq-RyMG9iz3n6b-hBhM1scLVsh2xXsNvvfaq9C5tpsbw69WWP4uIexJgcaayuARE0JsFFKXef0Eurb_cq1tusgzSLH6Y6VkAd7hS-7leAMOuWQQ9DZSe6IBJ4FZwwQ&v=404" onclick="searchlog(1,4158812,0,2,'','adwClk=1')">
				<img width="220" height="220" class="err-product" data-img="1" source-data-lazy-img="//img12.360buyimg.com/n7/jfs/t3781/362/2256425272/186486/853691ea/58467042N3bd1272a.jpg" />
</a>			<div data-lease="" data-catid="3997" data-venid="1000000984" data-presale=""></div>
		</div>
		<div class="p-scroll">
			<span class="ps-prev">&lt;</span>
			<span class="ps-next">&gt;</span>
			<div class="ps-wrap">
				<ul class="ps-main">
					<li class="ps-item"><a href="javascript:;" class="curr" title="灰色"><img data-url="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80MTU4ODEyLmh0bWw&log=89D2X8fH443l26lO_iBKNtU5A-4B-y9_kHAIaZc5bhGQ_bwwcAmL5l1hFfXjwQEDw5exHLdLXHsIKwslHK-Ais9w2TJ2EO4o5FlCyuUDUVQ8nVgkGqiKKPcLJaAxiGVqwEYEwhHoLcKkOQlxAm7DUBDEP8r4BP66NAuW2e9mpEQH12ioHZjk3UTrJ_5XIjYr9qKBaG9LDpyQPKOLbZUL9gGPfAciW-j0UyFdQKf5bJv8FunD9TGwtEreXt2q7__0Vg4tVIFVc8mXZ8U9xiXEIUo7ijr-Iq3PgqcbqFD6p5Ec80W_TBuZA5lMHclKoQJFvb6yQFvM-GkKX5oaAs35a6T3Fq-RyMG9iz3n6b-hBhM1scLVsh2xXsNvvfaq9C5tpsbw69WWP4uIexJgcaayuARE0JsFFKXef0Eurb_cq1tusgzSLH6Y6VkAd7hS-7leAMOuWQQ9DZSe6IBJ4FZwwQ&v=404"  data-presale="" data-sku="4158812" data-img="1" data-lazy-img="//img12.360buyimg.com/n9/jfs/t3781/362/2256425272/186486/853691ea/58467042N3bd1272a.jpg" class="err-product" width="25" height="25" /></a></li>
									</ul>
			</div>
		</div>
		<div class="p-price">
<strong class="J_4158812" data-done="1"><em>￥</em><i>109.00</i></strong>		</div>'''

plt=re.findall(r'￥</em><i>[\d\.]*',html)
tlt=re.findall(r'a target="_blank" title=".*?"',html)
print(plt,tlt)
for i in range(len(plt)):
    price = eval(plt[i].split('<i>')[1])
    title = eval(tlt[i].split('title=')[1])
print(price,title)