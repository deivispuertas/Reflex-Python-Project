"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[160],{9432:function(e,t,n){n.d(t,{q:function(){return v}});var[r,a]=(0,n(5227).k)({name:"AvatarStylesContext",hookName:"useAvatarStyles",providerName:"<Avatar/>"}),i=n(1337),l=n(5893);function o(e){var t;let n=e.split(" "),r=null!=(t=n.at(0))?t:"",a=n.length>1?n.at(-1):"";return r&&a?`${r.charAt(0)}${a.charAt(0)}`:r.charAt(0)}function s(e){let{name:t,getInitials:n,...r}=e,o=a();return(0,l.jsx)(i.m.div,{role:"img","aria-label":t,...r,__css:o.label,children:t?null==n?void 0:n(t):null})}s.displayName="AvatarName";var c=e=>(0,l.jsxs)(i.m.svg,{viewBox:"0 0 128 128",color:"#fff",width:"100%",height:"100%",className:"chakra-avatar__svg",...e,children:[(0,l.jsx)("path",{fill:"currentColor",d:"M103,102.1388 C93.094,111.92 79.3504,118 64.1638,118 C48.8056,118 34.9294,111.768 25,101.7892 L25,95.2 C25,86.8096 31.981,80 40.6,80 L87.4,80 C96.019,80 103,86.8096 103,95.2 L103,102.1388 Z"}),(0,l.jsx)("path",{fill:"currentColor",d:"M63.9961647,24 C51.2938136,24 41,34.2938136 41,46.9961647 C41,59.7061864 51.2938136,70 63.9961647,70 C76.6985159,70 87,59.7061864 87,46.9961647 C87,34.2938136 76.6985159,24 63.9961647,24"})]}),u=n(5721),d=n(7294);function m(e){let{src:t,srcSet:n,onError:r,onLoad:a,getInitials:o,name:m,borderRadius:f,loading:x,iconLabel:p,icon:h=(0,l.jsx)(c,{}),ignoreFallback:g,referrerPolicy:v,crossOrigin:y}=e,j=(0,u.d)({src:t,onError:r,crossOrigin:y,ignoreFallback:g});return t&&"loaded"===j?(0,l.jsx)(i.m.img,{src:t,srcSet:n,alt:m,onLoad:a,referrerPolicy:v,crossOrigin:null!=y?y:void 0,className:"chakra-avatar__img",loading:x,__css:{width:"100%",height:"100%",objectFit:"cover",borderRadius:f}}):m?(0,l.jsx)(s,{className:"chakra-avatar__initials",getInitials:o,name:m}):(0,d.cloneElement)(h,{role:"img","aria-label":p})}m.displayName="AvatarImage";var f=n(5059),x=n(1628),p=n(3672),h=n(5432),g={display:"inline-flex",alignItems:"center",justifyContent:"center",textAlign:"center",textTransform:"uppercase",fontWeight:"medium",position:"relative",flexShrink:0},v=(0,f.G)((e,t)=>{let n=(0,x.jC)("Avatar",e),[a,s]=(0,d.useState)(!1),{src:u,srcSet:f,name:v,showBorder:y,borderRadius:j="full",onError:_,onLoad:b,getInitials:N=o,icon:k=(0,l.jsx)(c,{}),iconLabel:S=" avatar",loading:C,children:E,borderColor:B,ignoreFallback:L,crossOrigin:w,...G}=(0,p.Lr)(e),A={borderRadius:j,borderWidth:y?"2px":void 0,...g,...n.container};return B&&(A.borderColor=B),(0,l.jsx)(i.m.span,{ref:t,...G,className:(0,h.cx)("chakra-avatar",e.className),"data-loaded":(0,h.PB)(a),__css:A,children:(0,l.jsxs)(r,{value:n,children:[(0,l.jsx)(m,{src:u,srcSet:f,loading:C,onLoad:(0,h.v0)(b,()=>{s(!0)}),onError:_,getInitials:N,name:v,borderRadius:j,icon:k,iconLabel:S,ignoreFallback:L,crossOrigin:w}),E]})})});v.displayName="Avatar"},5698:function(e,t,n){n.d(t,{z:function(){return p}});var r=n(7294),[a,i]=(0,n(5227).k)({strict:!1,name:"ButtonGroupContext"}),l=n(1337),o=n(5432),s=n(5893);function c(e){let{children:t,className:n,...a}=e,i=(0,r.isValidElement)(t)?(0,r.cloneElement)(t,{"aria-hidden":!0,focusable:!1}):t,c=(0,o.cx)("chakra-button__icon",n);return(0,s.jsx)(l.m.span,{display:"inline-flex",alignSelf:"center",flexShrink:0,...a,className:c,children:i})}c.displayName="ButtonIcon";var u=n(295);function d(e){let{label:t,placement:n,spacing:a="0.5rem",children:i=(0,s.jsx)(u.$,{color:"currentColor",width:"1em",height:"1em"}),className:c,__css:d,...m}=e,f=(0,o.cx)("chakra-button__spinner",c),x="start"===n?"marginEnd":"marginStart",p=(0,r.useMemo)(()=>({display:"flex",alignItems:"center",position:t?"relative":"absolute",[x]:t?a:0,fontSize:"1em",lineHeight:"normal",...d}),[d,t,x,a]);return(0,s.jsx)(l.m.div,{className:f,...m,__css:p,children:i})}d.displayName="ButtonSpinner";var m=n(5059),f=n(1628),x=n(3672),p=(0,m.G)((e,t)=>{let n=i(),a=(0,f.mq)("Button",{...n,...e}),{isDisabled:c=null==n?void 0:n.isDisabled,isLoading:u,isActive:m,children:p,leftIcon:g,rightIcon:v,loadingText:y,iconSpacing:j="0.5rem",type:_,spinner:b,spinnerPlacement:N="start",className:k,as:S,...C}=(0,x.Lr)(e),E=(0,r.useMemo)(()=>{let e={...null==a?void 0:a._focus,zIndex:1};return{display:"inline-flex",appearance:"none",alignItems:"center",justifyContent:"center",userSelect:"none",position:"relative",whiteSpace:"nowrap",verticalAlign:"middle",outline:"none",...a,...!!n&&{_focus:e}}},[a,n]),{ref:B,type:L}=function(e){let[t,n]=(0,r.useState)(!e);return{ref:(0,r.useCallback)(e=>{e&&n("BUTTON"===e.tagName)},[]),type:t?"button":void 0}}(S),w={rightIcon:v,leftIcon:g,iconSpacing:j,children:p};return(0,s.jsxs)(l.m.button,{ref:function(...e){return(0,r.useMemo)(()=>(function(...e){return t=>{e.forEach(e=>{!function(e,t){if(null!=e){if("function"==typeof e){e(t);return}try{e.current=t}catch(n){throw Error(`Cannot assign value '${t}' to ref '${e}'`)}}}(e,t)})}})(...e),e)}(t,B),as:S,type:null!=_?_:L,"data-active":(0,o.PB)(m),"data-loading":(0,o.PB)(u),__css:E,className:(0,o.cx)("chakra-button",k),...C,disabled:c||u,children:[u&&"start"===N&&(0,s.jsx)(d,{className:"chakra-button__spinner--start",label:y,placement:"start",spacing:j,children:b}),u?y||(0,s.jsx)(l.m.span,{opacity:0,children:(0,s.jsx)(h,{...w})}):(0,s.jsx)(h,{...w}),u&&"end"===N&&(0,s.jsx)(d,{className:"chakra-button__spinner--end",label:y,placement:"end",spacing:j,children:b})]})});function h(e){let{leftIcon:t,rightIcon:n,children:r,iconSpacing:a}=e;return(0,s.jsxs)(s.Fragment,{children:[t&&(0,s.jsx)(c,{marginEnd:a,children:t}),r,n&&(0,s.jsx)(c,{marginStart:a,children:n})]})}p.displayName="Button"},5721:function(e,t,n){n.d(t,{d:function(){return i},z:function(){return l}});var r=n(6245),a=n(7294);function i(e){let{loading:t,src:n,srcSet:i,onLoad:l,onError:o,crossOrigin:s,sizes:c,ignoreFallback:u}=e,[d,m]=(0,a.useState)("pending");(0,a.useEffect)(()=>{m(n?"loading":"pending")},[n]);let f=(0,a.useRef)(),x=(0,a.useCallback)(()=>{if(!n)return;p();let e=new Image;e.src=n,s&&(e.crossOrigin=s),i&&(e.srcset=i),c&&(e.sizes=c),t&&(e.loading=t),e.onload=e=>{p(),m("loaded"),null==l||l(e)},e.onerror=e=>{p(),m("failed"),null==o||o(e)},f.current=e},[n,s,i,c,l,o,t]),p=()=>{f.current&&(f.current.onload=null,f.current.onerror=null,f.current=null)};return(0,r.G)(()=>{if(!u)return"loading"===d&&x(),()=>{p()}},[d,x,u]),u?"loaded":d}var l=(e,t)=>"loaded"!==e&&"beforeLoadOrError"===t||"failed"===e&&"onError"===t},1941:function(e,t,n){n.d(t,{E:function(){return s}});var r=n(5059),a=n(5893),i=(0,r.G)(function(e,t){let{htmlWidth:n,htmlHeight:r,alt:i,...l}=e;return(0,a.jsx)("img",{width:n,height:r,ref:t,alt:i,...l})});i.displayName="NativeImage";var l=n(5721),o=n(1337),s=(0,r.G)(function(e,t){let{fallbackSrc:n,fallback:r,src:s,srcSet:c,align:u,fit:d,loading:m,ignoreFallback:f,crossOrigin:x,fallbackStrategy:p="beforeLoadOrError",referrerPolicy:h,...g}=e,v=void 0!==n||void 0!==r,y=null!=m||f||!v,j=(0,l.d)({...e,crossOrigin:x,ignoreFallback:y}),_=(0,l.z)(j,p),b={ref:t,objectFit:d,objectPosition:u,...y?g:function(e,t=[]){let n=Object.assign({},e);for(let e of t)e in n&&delete n[e];return n}(g,["onError","onLoad"])};return _?r||(0,a.jsx)(o.m.img,{as:i,className:"chakra-image__placeholder",src:n,...b}):(0,a.jsx)(o.m.img,{as:i,src:s,srcSet:c,crossOrigin:x,loading:m,referrerPolicy:h,className:"chakra-image",...b})});s.displayName="Image"},7754:function(e,t,n){n.d(t,{M:function(){return l}});var r=n(1337),a=n(5059),i=n(5893),l=(0,r.m)("div",{baseStyle:{display:"flex",alignItems:"center",justifyContent:"center"}});l.displayName="Center";var o={horizontal:{insetStart:"50%",transform:"translateX(-50%)"},vertical:{top:"50%",transform:"translateY(-50%)"},both:{insetStart:"50%",top:"50%",transform:"translate(-50%, -50%)"}};(0,a.G)(function(e,t){let{axis:n="both",...a}=e;return(0,i.jsx)(r.m.div,{ref:t,__css:o[n],...a,position:"absolute"})})},3100:function(e,t,n){n.d(t,{xu:function(){return l}});var r=n(1337),a=n(5059),i=n(5893),l=(0,r.m)("div");l.displayName="Box";var o=(0,a.G)(function(e,t){let{size:n,centerContent:r=!0,...a}=e;return(0,i.jsx)(l,{ref:t,boxSize:n,__css:{...r?{display:"flex",alignItems:"center",justifyContent:"center"}:{},flexShrink:0,flexGrow:0},...a})});o.displayName="Square",(0,a.G)(function(e,t){let{size:n,...r}=e;return(0,i.jsx)(o,{size:n,ref:t,borderRadius:"9999px",...r})}).displayName="Circle"},5034:function(e,t,n){n.d(t,{L:function(){return r}});var r=(0,n(1337).m)("div",{baseStyle:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}});r.displayName="Spacer"},4418:function(e,t,n){n.d(t,{X:function(){return c}});var r=n(5059),a=n(1628),i=n(3672),l=n(1337),o=n(5432),s=n(5893),c=(0,r.G)(function(e,t){let n=(0,a.mq)("Heading",e),{className:r,...c}=(0,i.Lr)(e);return(0,s.jsx)(l.m.h2,{ref:t,className:(0,o.cx)("chakra-heading",e.className),...c,__css:n})});c.displayName="Heading"},4641:function(e,t,n){n.d(t,{U:function(){return l}});var r=n(7073),a=n(5059),i=n(5893),l=(0,a.G)((e,t)=>(0,i.jsx)(r.K,{align:"center",...e,direction:"row",ref:t}));l.displayName="HStack"},204:function(e,t,n){n.d(t,{k:function(){return l}});var r=n(5059),a=n(1337),i=n(5893),l=(0,r.G)(function(e,t){let{direction:n,align:r,justify:l,wrap:o,basis:s,grow:c,shrink:u,...d}=e;return(0,i.jsx)(a.m.div,{ref:t,__css:{display:"flex",flexDirection:n,alignItems:r,justifyContent:l,flexWrap:o,flexBasis:s,flexGrow:c,flexShrink:u},...d})});l.displayName="Flex"},1669:function(e,t,n){n.d(t,{g:function(){return l}});var r=n(7073),a=n(5059),i=n(5893),l=(0,a.G)((e,t)=>(0,i.jsx)(r.K,{align:"center",...e,direction:"column",ref:t}));l.displayName="VStack"},7073:function(e,t,n){n.d(t,{K:function(){return d}});var r=n(1337),a=n(5893),i=e=>(0,a.jsx)(r.m.div,{className:"chakra-stack__item",...e,__css:{display:"inline-block",flex:"0 0 auto",minWidth:0,...e.__css}});i.displayName="StackItem";var l=n(5432);function o(e,t){return Array.isArray(e)?e.map(e=>null===e?null:t(e)):(0,l.Kn)(e)?Object.keys(e).reduce((n,r)=>(n[r]=t(e[r]),n),{}):null!=e?t(e):null}Object.freeze(["base","sm","md","lg","xl","2xl"]);var s="& > *:not(style) ~ *:not(style)",c=n(5059),u=n(7294),d=(0,c.G)((e,t)=>{let{isInline:n,direction:c,align:d,justify:m,spacing:f="0.5rem",wrap:x,children:p,divider:h,className:g,shouldWrapChildren:v,...y}=e,j=n?"row":null!=c?c:"column",_=(0,u.useMemo)(()=>(function(e){let{spacing:t,direction:n}=e,r={column:{marginTop:t,marginEnd:0,marginBottom:0,marginStart:0},row:{marginTop:0,marginEnd:0,marginBottom:0,marginStart:t},"column-reverse":{marginTop:0,marginEnd:0,marginBottom:t,marginStart:0},"row-reverse":{marginTop:0,marginEnd:t,marginBottom:0,marginStart:0}};return{flexDirection:n,[s]:o(n,e=>r[e])}})({direction:j,spacing:f}),[j,f]),b=(0,u.useMemo)(()=>(function(e){let{spacing:t,direction:n}=e,r={column:{my:t,mx:0,borderLeftWidth:0,borderBottomWidth:"1px"},"column-reverse":{my:t,mx:0,borderLeftWidth:0,borderBottomWidth:"1px"},row:{mx:t,my:0,borderLeftWidth:"1px",borderBottomWidth:0},"row-reverse":{mx:t,my:0,borderLeftWidth:"1px",borderBottomWidth:0}};return{"&":o(n,e=>r[e])}})({spacing:f,direction:j}),[f,j]),N=!!h,k=!v&&!N,S=(0,u.useMemo)(()=>{let e=u.Children.toArray(p).filter(e=>(0,u.isValidElement)(e));return k?e:e.map((t,n)=>{let r=void 0!==t.key?t.key:n,l=n+1===e.length,o=(0,a.jsx)(i,{children:t},r),s=v?o:t;if(!N)return s;let c=(0,u.cloneElement)(h,{__css:b});return(0,a.jsxs)(u.Fragment,{children:[s,l?null:c]},r)})},[h,b,N,k,v,p]),C=(0,l.cx)("chakra-stack",g);return(0,a.jsx)(r.m.div,{ref:t,display:"flex",alignItems:d,justifyContent:m,flexDirection:_.flexDirection,flexWrap:x,className:C,__css:N?{}:{[s]:_[s]},...y,children:S})});d.displayName="Stack"},9564:function(e,t,n){n.d(t,{x:function(){return c}});var r=n(5059),a=n(1628),i=n(3672),l=n(1337),o=n(5432),s=n(5893),c=(0,r.G)(function(e,t){let n=(0,a.mq)("Text",e),{className:r,align:c,decoration:u,casing:d,...m}=(0,i.Lr)(e),f=function(e){let t=Object.assign({},e);for(let e in t)void 0===t[e]&&delete t[e];return t}({textAlign:e.align,textDecoration:e.decoration,textTransform:e.casing});return(0,s.jsx)(l.m.p,{ref:t,className:(0,o.cx)("chakra-text",e.className),...f,...m,__css:n})});c.displayName="Text"},3838:function(e,t,n){n.d(t,{r:function(){return c}});var r=n(5059),a=n(1628),i=n(3672),l=n(1337),o=n(5432),s=n(5893),c=(0,r.G)(function(e,t){let n=(0,a.mq)("Link",e),{className:r,isExternal:c,...u}=(0,i.Lr)(e);return(0,s.jsx)(l.m.a,{target:c?"_blank":void 0,rel:c?"noopener":void 0,ref:t,className:(0,o.cx)("chakra-link",r),...u,__css:n})});c.displayName="Link"}}]);