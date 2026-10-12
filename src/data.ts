export const creator = { name: 'Shruti', handle: '@_.shru_.ti19', instagram: 'https://www.instagram.com/_.shru_.ti19/', tagline: 'Beauty. Style. Lifestyle. Stories that connect.', mediaKit: '/shruti-media-kit.pdf' };
export const categories = ['All', 'Beauty', 'Fashion', 'Lifestyle', 'Brand Collaborations', 'PR & Unboxing'];
export type Work = { id: string; title: string; category: string; format: 'Photo' | 'Reel'; image: string; url: string; alt: string };
export const work: Work[] = [
 {id:'DdVjyDIjujj', title:'A little everyday magic',category:'Lifestyle',format:'Photo',image:'/images/hero.webp',url:'https://www.instagram.com/_.shru_.ti19/p/DdVjyDIjujj/',alt:'Shruti in a cream blouse and jeans at a leafy outdoor café'},
 {id:'Dc6KEw4jhpT',title:'Style, with a story',category:'Fashion',format:'Photo',image:'/images/heritage.webp',url:'https://www.instagram.com/_.shru_.ti19/p/Dc6KEw4jhpT/',alt:'Shruti wearing a colourful top and wide-leg jeans among carved stone columns'},
 {id:'DeWjcP0kzzA',title:'Main character energy',category:'Fashion',format:'Photo',image:'/images/evening.webp',url:'https://www.instagram.com/_.shru_.ti19/p/DeWjcP0kzzA/',alt:'Shruti posing in a red outfit against a dramatic blue floral backdrop'},
 {id:'DeOCHpWTJ2-',title:'The beauty edit',category:'Beauty',format:'Reel',image:'/images/beauty.webp',url:'https://www.instagram.com/_.shru_.ti19/reel/DeOCHpWTJ2-/',alt:'Original thumbnail from Shruti’s beauty and personal style reel'},
 {id:'Db_ErIbjSpW',title:'Off-duty, on my own terms',category:'Lifestyle',format:'Photo',image:'/images/off-duty.webp',url:'https://www.instagram.com/_.shru_.ti19/p/Db_ErIbjSpW/',alt:'Shruti sitting on a motorcycle in a casual white top and blue jeans'},
 {id:'DeThp-vzKgz',title:'After-hours stories',category:'Lifestyle',format:'Reel',image:'/images/after-hours.webp',url:'https://www.instagram.com/_.shru_.ti19/reel/DeThp-vzKgz/',alt:'Shruti outside a warmly lit café at night'}
];
export const collaborations = [
 {title:'Paid partnerships',type:'Paid Collaboration',number:'01',copy:'Your brief, my creative lens. Dedicated reels, product features and thoughtful campaign content.',detail:'Sponsored reels · Product features · Brand campaigns'},
 {title:'Barter collaborations',type:'Barter Collaboration',number:'02',copy:'A lovely product. A natural fit. Product-for-content partnerships with deliverables agreed together.',detail:'Product exchanges · Fashion edits · Lifestyle features'},
 {title:'PR & gifting',type:'PR / Gifting',number:'03',copy:'Discoveries worth sharing, from a beautiful unboxing to a first impression.',detail:'Coverage and deliverables agreed in advance.'},
 {title:'Creative content',type:'UGC / Content Creation',number:'04',copy:'Have a UGC idea for your own channels? Let’s explore a creator-led concept and what’s possible.',detail:'Formats, usage rights and availability discussed together.'}
];
// Publish these sections only when approved, genuine content is supplied.
export const brands: {name:string;logo:string;url:string}[] = [];
export const campaigns: {name:string;objective:string;concept:string;deliverables:string;image:string;url:string}[] = [];
export const testimonials: {quote:string;name:string}[] = [];
