(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[3709],{24487:function(e,r,t){"use strict";t.d(r,{At:function(){return m},aG:function(){return v},gN:function(){return g}});var n=t(32393),i=t(14007),o=t(49031),s=t(27378);function a(){return a=Object.assign||function(e){for(var r=1;r<arguments.length;r++){var t=arguments[r];for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&(e[n]=t[n])}return e},a.apply(this,arguments)}function c(e,r){if(null==e)return{};var t,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)t=o[n],r.indexOf(t)>=0||(i[t]=e[t]);return i}var l=["spacing"],u=["isCurrentPage","as","className","href"],d=["isCurrentPage","separator","isLastChild","spacing","children","className"],p=["children","spacing","separator","className"],f=(0,n.Gp)((function(e,r){var t=e.spacing,i=c(e,l),o=a({mx:t},(0,n.yK)().separator);return s.createElement(n.m$.span,a({ref:r,role:"presentation"},i,{__css:o}))}));i.Ts&&(f.displayName="BreadcrumbSeparator");var m=(0,n.Gp)((function(e,r){var t=e.isCurrentPage,o=e.as,l=e.className,d=e.href,p=c(e,u),f=(0,n.yK)(),m=a({ref:r,as:o,className:(0,i.cx)("chakra-breadcrumb__link",l)},p);return t?s.createElement(n.m$.span,a({"aria-current":"page",__css:f.link},m)):s.createElement(n.m$.a,a({__css:f.link,href:d},m))}));i.Ts&&(m.displayName="BreadcrumbLink");var g=(0,n.Gp)((function(e,r){var t=e.isCurrentPage,l=e.separator,u=e.isLastChild,p=e.spacing,g=e.children,v=e.className,h=c(e,d),b=(0,o.WR)(g).map((function(e){return e.type===m?s.cloneElement(e,{isCurrentPage:t}):e.type===f?s.cloneElement(e,{spacing:p,children:e.props.children||l}):e})),y=a({display:"inline-flex",alignItems:"center"},(0,n.yK)().item),x=(0,i.cx)("chakra-breadcrumb__list-item",v);return s.createElement(n.m$.li,a({ref:r,className:x},h,{__css:y}),b,!u&&s.createElement(f,{spacing:p},l))}));i.Ts&&(g.displayName="BreadcrumbItem");var v=(0,n.Gp)((function(e,r){var t=(0,n.jC)("Breadcrumb",e),l=(0,n.Lr)(e),u=l.children,d=l.spacing,f=void 0===d?"0.5rem":d,m=l.separator,g=void 0===m?"/":m,v=l.className,h=c(l,p),b=(0,o.WR)(u),y=b.length,x=b.map((function(e,r){return s.cloneElement(e,{separator:g,spacing:f,isLastChild:y===r+1})})),j=(0,i.cx)("chakra-breadcrumb",v);return s.createElement(n.m$.nav,a({ref:r,"aria-label":"breadcrumb",className:j,__css:t.container},h),s.createElement(n.Fo,{value:t},s.createElement(n.m$.ol,{className:"chakra-breadcrumb__list"},x)))}));i.Ts&&(v.displayName="Breadcrumb")},55447:function(e,r,t){"use strict";var n=t(90849),i=t(60530),o=t(34896),s=t(29549),a=t(24246);function c(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function l(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?c(Object(t),!0).forEach((function(r){(0,n.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):c(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}r.Z=function(e){var r=e.isOpen,t=e.onClose,n=e.onConfirm,c=e.title,u=e.message,d=e.cancelButtonText,p=e.cancelButtonThemingProps,f=e.continueButtonText,m=e.continueButtonThemingProps,g=e.isLoading,v=e.returnFocusOnClose,h=e.isCentered,b=e.testId,y=void 0===b?"confirmation-modal":b,x=e.icon;return(0,a.jsxs)(i.u_,{isOpen:r,onClose:t,size:"lg",returnFocusOnClose:null===v||void 0===v||v,isCentered:h,children:[(0,a.jsx)(i.ZA,{}),(0,a.jsxs)(i.hz,{textAlign:"center",p:6,"data-testid":y,children:[x?(0,a.jsx)(o.M5,{mb:2,children:x}):null,c?(0,a.jsx)(i.xB,{fontWeight:"medium",pb:0,children:c}):null,u?(0,a.jsx)(i.fe,{children:u}):null,(0,a.jsx)(i.mz,{children:(0,a.jsxs)(o.MI,{columns:2,width:"100%",children:[(0,a.jsx)(s.zx,l(l({variant:"outline",mr:3,onClick:t,"data-testid":"cancel-btn",isDisabled:g},p),{},{children:d||"Cancel"})),(0,a.jsx)(s.zx,l(l({colorScheme:"primary",onClick:n,"data-testid":"continue-btn",isLoading:g},m),{},{children:f||"Continue"}))]})})]})]})}},8800:function(e,r,t){"use strict";t.d(r,{Q:function(){return o}});var n=t(13018),i=t(24246),o=(0,n.IU)({displayName:"SparkleIcon",viewBox:"0 0 18 18",path:(0,i.jsx)("path",{fill:"currentColor",d:"M9.53604 15.8107C9.81449 15.8107 10.0158 15.6256 10.0681 15.3471C10.7648 11.6208 11.1324 11.0552 14.8315 10.559C15.1373 10.518 15.3337 10.303 15.3337 10.0245C15.3337 9.74611 15.1373 9.53357 14.8315 9.49254C11.1609 8.99636 10.6349 8.45671 10.0681 4.71568C10.0246 4.42354 9.81449 4.22717 9.53604 4.22717C9.28 4.22717 9.05872 4.41234 9.01768 4.70447C8.34835 8.43318 7.95089 8.99143 4.24063 9.49254C3.94849 9.53357 3.74963 9.74611 3.74963 10.0245C3.74963 10.303 3.94849 10.5155 4.24063 10.559C7.91753 11.0847 8.446 11.5836 9.01768 15.3359C9.04995 15.6256 9.26003 15.8107 9.53604 15.8107ZM3.62366 7.96543C3.82881 7.96543 3.9954 7.81253 4.03397 7.60739C4.40352 5.74358 4.25772 5.75481 6.22471 5.41918C6.44356 5.38938 6.58033 5.21404 6.58033 5.0089C6.58033 4.81497 6.44109 4.63717 6.22471 4.5986C4.26265 4.27148 4.40105 4.26655 4.03397 2.43529C3.9954 2.22768 3.84249 2.06358 3.62366 2.06358C3.41604 2.06358 3.26314 2.21648 3.21335 2.43529C2.84873 4.25179 2.9896 4.25179 1.02259 4.5986C0.814976 4.63963 0.666992 4.81497 0.666992 5.0089C0.666992 5.23894 0.814976 5.38938 1.05241 5.41918C2.98714 5.74249 2.84626 5.73868 3.21335 7.58252C3.26314 7.80132 3.40483 7.96543 3.62366 7.96543ZM8.03377 3.9032C8.17054 3.9032 8.27749 3.80747 8.30485 3.6707C8.5461 2.4508 8.47882 2.4732 9.75105 2.22703C9.89903 2.19969 9.9923 2.09273 9.9923 1.95599C9.9923 1.81922 9.89656 1.71472 9.74858 1.68738C8.46759 1.43874 8.52367 1.43874 8.30485 0.254909C8.27749 0.106937 8.18175 0 8.03377 0C7.897 0 7.80126 0.106939 7.76269 0.257375C7.50393 1.43874 7.60488 1.43874 6.31652 1.68738C6.16851 1.71472 6.08647 1.81922 6.08647 1.95599C6.08647 2.10396 6.16851 2.19723 6.33265 2.22703C7.60488 2.43956 7.50393 2.45079 7.76269 3.64827C7.80126 3.80747 7.897 3.9032 8.03377 3.9032Z"})})},29073:function(e,r,t){"use strict";var n=t(34896),i=t(73452),o=t(24246);r.Z=function(e){var r=e.title,t=e.description,s=e.button;return(0,o.jsxs)(n.Ug,{backgroundColor:"gray.50",border:"1px solid",borderColor:"blue.400",borderRadius:"md",justifyContent:"space-between",py:4,px:6,"data-testid":"empty-state",children:[(0,o.jsx)(i.ii,{alignSelf:"start",color:"blue.400",mt:.5}),(0,o.jsxs)(n.xu,{flexGrow:1,children:[(0,o.jsx)(n.xv,{fontWeight:"bold",fontSize:"sm",mb:1,children:r}),(0,o.jsx)(n.xv,{fontSize:"sm",color:"gray.600",lineHeight:"5",children:t})]}),s]})}},82466:function(e,r,t){"use strict";var n=t(90089),i=t(90849),o=t(40240),s=t(34896),a=t(55422),c=t(24246),l=t(27378),u=["key"],d=["key"];function p(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function f(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?p(Object(t),!0).forEach((function(r){(0,i.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):p(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}r.Z=function(e){var r=e.rowHeading,t=e.renderRowSubheading,i=e.renderOverflowMenu,p=e.rows,m=e.prepareRow,g=e.getTableBodyProps,v=e.onSubrowClick;return(0,c.jsx)(o.p3,f(f({backgroundColor:a.p},g()),{},{children:p.map((function(e){return m(e),[(0,l.createElement)(o.Tr,f(f({},e.getRowProps()),{},{borderTopLeftRadius:"6px",borderTopRightRadius:"6px",backgroundColor:"gray.50",borderWidth:"1px",borderBottom:"none",mt:4,ml:4,mr:4,key:e.groupByVal,"data-testid":"grouped-row-".concat(e.groupByVal)}),(0,c.jsxs)(o.Td,f(f({display:"flex",justifyContent:"space-between",colSpan:e.cells.length},e.cells[0].getCellProps()),{},{width:"auto",paddingX:2,children:[(0,c.jsxs)(s.Kq,{children:[r?(0,c.jsx)(s.xv,{fontSize:"xs",lineHeight:4,fontWeight:"500",color:"gray.600",textTransform:"uppercase",pb:2,pt:1,children:r}):null,(0,c.jsx)(s.xv,{fontSize:"sm",lineHeight:5,fontWeight:"bold",color:"gray.600",mb:1,children:t(e)})]}),i?i(e):null]}))),e.subRows.map((function(r,t){m(r);var i=r.getRowProps(),s=i.key,a=(0,n.Z)(i,u);return(0,c.jsx)(o.Tr,f(f({minHeight:9,borderWidth:"1px",borderColor:"gray.200",borderTop:"none",borderBottomLeftRadius:t===e.subRows.length-1?"6px":"",borderBottomRightRadius:t===e.subRows.length-1?"6px":""},a),{},{_hover:{bg:"gray.50"},cursor:v?"pointer":void 0,backgroundColor:"white",onClick:v?function(){return v(r)}:void 0,ml:4,mr:4,_last:{mb:4},children:r.cells.map((function(e,t){var i=e.getCellProps(),s=i.key,a=(0,n.Z)(i,d);return(0,c.jsx)(o.Td,f(f({},a),{},{borderRightWidth:t===r.cells.length-1?"":"1px",borderBottom:"none",borderColor:"gray.200",padding:0,"data-testid":"subrow-".concat(s),children:e.render("Cell")}),s)}))}),s)}))]}))}))}},99725:function(e,r,t){"use strict";var n=t(90849),i=t(90089),o=t(40240),s=t(34896),a=t(55422),c=t(24246),l=["key"],u=["key"];function d(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function p(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?d(Object(t),!0).forEach((function(r){(0,n.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):d(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var f=function(){return(0,c.jsx)(o.Th,{padding:0,margin:0,width:4,borderBottomColor:"gray.200",boxSizing:"border-box"})};r.Z=function(e){var r=e.headerGroups;return(0,c.jsx)(o.hr,{position:"sticky",top:"0px",height:"36px",zIndex:10,backgroundColor:a.p,children:r.map((function(e){var r=e.getHeaderGroupProps(),t=r.key,n=(0,i.Z)(r,l);return(0,c.jsxs)(o.Tr,p(p({},n),{},{height:"inherit",children:[(0,c.jsx)(f,{}),e.headers.map((function(e,r){var t=e.getHeaderProps(),n=t.key,a=(0,i.Z)(t,u);return(0,c.jsxs)(o.Th,p(p({},a),{},{title:"".concat(e.Header),textTransform:"none",px:2,display:"flex",alignItems:"center",borderLeftWidth:0===r?"1px":"",borderRightWidth:"1px",borderColor:"gray.200",children:[(0,c.jsx)(s.xv,{whiteSpace:"nowrap",textOverflow:"ellipsis",overflow:"hidden",mr:1,children:e.render("Header")}),e.canResize&&(0,c.jsx)(s.xu,p(p({},e.getResizerProps()),{},{position:"absolute",top:0,right:0,width:2,height:"100%",css:{touchAction:":none"}}))]}),n)})),(0,c.jsx)(f,{})]}),t)}))})}},55422:function(e,r,t){"use strict";t.d(r,{p:function(){return n}});var n="#F7F7F7"},24753:function(e,r,t){"use strict";t.d(r,{MA:function(){return u},Vo:function(){return p},t5:function(){return d}});var n=t(90849),i=t(34896),o=t(24246);function s(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function a(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?s(Object(t),!0).forEach((function(r){(0,n.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):s(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var c=function(e){var r=e.message;return(0,o.jsxs)(i.xv,{"data-testid":"toast-success-msg",children:[(0,o.jsx)("strong",{children:"Success:"})," ",r]})},l=function(e){var r=e.message;return(0,o.jsxs)(i.xv,{"data-testid":"toast-error-msg",children:[(0,o.jsx)("strong",{children:"Error:"})," ",r]})},u={variant:"subtle",position:"top",description:"",duration:5e3,status:"success",isClosable:!0},d=function(e){var r=(0,o.jsx)(c,{message:e});return a(a({},u),{description:r})},p=function(e){var r=(0,o.jsx)(l,{message:e});return a(a({},u),{description:r,status:"error"})}},37761:function(e,r,t){"use strict";t.d(r,{E:function(){return n}});var n=function(e){return e.toLowerCase().replace(/ /g,"_").replace(/[^a-zA-Z0-9._<>-]/g,"")}},16446:function(e,r,t){"use strict";t.d(r,{U:function(){return n}});var n=function(e){var r,t=e.data_categories.flatMap((function(e){return e.split(",")}));return{data_use:e.data_use,data_categories:t,features:e.features,legal_basis_for_processing:e.legal_basis_for_processing,flexible_legal_basis_for_processing:e.flexible_legal_basis_for_processing,retention_period:"".concat(e.retention_period),cookies:null===(r=e.cookies)||void 0===r?void 0:r.map((function(e){return{name:e.name,domain:e.domain,path:e.path}}))}}},96085:function(e,r,t){"use strict";t.r(r),t.d(r,{default:function(){return fe}});var n=t(34896),i=t(24487),o=t(79894),s=t.n(o),a=t(27378),c=t(51471),l=t(60709),u=t(83125),d=t(29073),p=t(73679),f=t(90089),m=t(55732),g=t(97865),v=t(90849),h=t(34707),b=t.n(h),y=t(21084),x=t(70409),j=t(29549),O=t(34090),_=t(68301),C=t(6848),k=t(90768),w=t(43139),P={name:"",consent_use:"",data_use:"",data_categories:["user"],cookieNames:[],cookies:[]},S=[{label:"Analytics",value:"analytics",description:"Provides analytics for activities such as system and advertising performance reporting, insights and fraud detection."},{label:"Essential",value:"essential",description:"Operates the service or product, including legal obligations, support and basic system operations."},{label:"Functional",value:"functional",description:"Used for specific, necessary, and legitimate purposes."},{label:"Marketing",value:"marketing",description:"Enables marketing, promotion, advertising and sales activities for the product, service, application or system."}],E=function(e){return S.some((function(r){return r.value===e.split(".")[0]}))},D=t(37761),Z=t(44047),N=t(48466),z=t(78624),R=t(24753),T=t(60530),B=t(8800),A=t(24246),F=function(e){var r=e.title,t=e.children,i=e.isOpen,o=e.onClose,s=e.onSuggestionClick,a=e.suggestionsState,c=(0,k.hz)();return(0,A.jsxs)(T.u_,{isOpen:i,onClose:o,isCentered:!0,scrollBehavior:"inside",size:"xl",children:[(0,A.jsx)(T.ZA,{}),(0,A.jsxs)(T.hz,{textAlign:"left",p:0,children:[(0,A.jsx)(T.xB,{p:0,children:(0,A.jsxs)(n.xu,{backgroundColor:"gray.50",px:6,py:4,border:"1px",borderColor:"gray.200",borderTopRadius:6,display:"flex",justifyContent:"space-between",alignItems:"center",children:[(0,A.jsx)(n.X6,{as:"h3",size:"sm",children:r}),c.dictionaryService?(0,A.jsx)(j.hU,{icon:(0,A.jsx)(B.Q,{color:"showing"===a?"complimentary.500":void 0}),"aria-label":"See compass suggestions",variant:"outline",borderColor:"gray.200",onClick:s,isDisabled:"disabled"===a,"data-testid":"sparkle-btn"}):null]})}),(0,A.jsx)(T.fe,{pb:4,overflow:"scroll",children:t})]})]})},V=t(75846),M=t(16446),W=function(e){var r=e.index,t=e.isSuggestion,i=(0,C.C)(V.oW),o=t?"complimentary.500":"gray.800",s=(0,O.u6)().values,a=i.filter((function(e){return e.value.split(".")[0]===s.privacy_declarations[r].consent_use}));return(0,A.jsxs)(n.gC,{width:"100%",borderRadius:"4px",border:"1px solid",borderColor:"gray.200",spacing:4,p:4,children:[(0,A.jsx)(w.AP,{label:"Data use",tooltip:"What is the system using the data for. For example, is it for third party advertising or perhaps simply providing system operations.",name:"privacy_declarations.".concat(r,".consent_use"),options:S,variant:"stacked",isRequired:!0,isCustomOption:!0,singleValueBlock:!0,textColor:o}),(0,A.jsx)(w.AP,{label:"Detailed data use (optional)",tooltip:"Select a more specific data use",name:"privacy_declarations.".concat(r,".data_use"),options:a,variant:"stacked",isCustomOption:!0,singleValueBlock:!0,textColor:o,isDisabled:!s.privacy_declarations[r].consent_use}),(0,A.jsx)(w.VT,{label:"Cookie names",name:"privacy_declarations.".concat(r,".cookieNames"),options:[],variant:"stacked",isMulti:!0,textColor:o})]})},L=function(e){var r=e.showSuggestions,t=(0,O.u6)(),n=t.values,i=t.setFieldValue,o=n.vendor_id,s=(0,Z.Wp)({vendor_id:o},{skip:!r||null==o}).isLoading,c=(0,C.C)((0,Z.cL)(o||""));return(0,a.useEffect)((function(){if(r&&n.vendor_id&&null!==c&&void 0!==c&&c.length){var e=c.filter((function(e){return E(e.data_use)})).map((function(e){return(0,M.U)(e)})).map((function(e){var r,t,n;return{name:null!==(r=e.name)&&void 0!==r?r:"",consent_use:e.data_use.split(".")[0],data_use:e.data_use,data_categories:e.data_categories,cookieNames:(null===(t=e.cookies)||void 0===t?void 0:t.map((function(e){return e.name})))||[],cookies:null!==(n=e.cookies)&&void 0!==n?n:[]}}));i("privacy_declarations",e)}}),[r,n.vendor_id,c,i]),s?(0,A.jsx)(u.$,{size:"sm",alignSelf:"center"}):(0,A.jsx)(O.F2,{name:"privacy_declarations",render:function(e){var t,i;return(0,A.jsxs)(A.Fragment,{children:[n.privacy_declarations.map((function(e,t){return(0,A.jsx)(W,{index:t,isSuggestion:r},e.data_use||t)})),(0,A.jsx)(j.zx,{size:"xs",variant:"ghost",colorScheme:"complimentary",onClick:function(){e.push(P)},disabled:(null===(t=n.privacy_declarations[n.privacy_declarations.length-1])||void 0===t?void 0:t.data_use)===P.data_use&&(null===(i=n.privacy_declarations[n.privacy_declarations.length-1])||void 0===i?void 0:i.consent_use)===P.consent_use,"data-testid":"add-data-use-btn",children:"Add data use +"})]})}})},G=["cookieNames","consent_use"];function I(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function H(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?I(Object(t),!0).forEach((function(r){(0,v.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):I(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var U={name:"",vendor_id:void 0,privacy_declarations:[P]},q=_.Ry().shape({name:_.Z_().required().label("Vendor name")}),$=_.Ry().shape({vendor_id:_.Z_().when("name",{is:function(e){return""===e||null},then:_.Z_().required().label("Vendor"),otherwise:_.Z_().nullable().label("Vendor")}),name:_.Z_().when("vendor_id",{is:function(e){return""===e||null},then:_.Z_().required().label("Name"),otherwise:_.Z_().nullable().label("Name")})},[["name","vendor_id"]]),X=function(e){var r,t=e.passedInSystem,i=e.onCloseModal,o=(0,y.qY)(),s=H(H({},o),{},{isOpen:!!t||o.isOpen}),c=(0,x.pm)(),l=(0,k.hz)().dictionaryService,u=(0,Z.Rd)(void 0,{skip:!l}).isLoading,d=(0,C.C)(Z.o),v=(0,N.f7)(),h=(0,g.Z)(v,1)[0],_=(0,N.qQ)(),S=(0,g.Z)(_,1)[0],T=(0,a.useState)(!1),B=T[0],V=T[1],M=function(){s.onClose(),i&&i(),V(!1)},W=t?{name:null!==(r=t.name)&&void 0!==r?r:"",vendor_id:t.vendor_id,privacy_declarations:t.privacy_declarations.filter((function(e){return E(e.data_use)})).map((function(e){var r,t;return H(H({},e),{},{name:null!==(r=e.name)&&void 0!==r?r:"",cookies:null!==(t=e.cookies)&&void 0!==t?t:[],cookieNames:e.cookies?e.cookies.map((function(e){return e.name})):[],consent_use:e.data_use.split(".")[0]})}))}:U,I=function(){var e=(0,m.Z)(b().mark((function e(r,n){var i,o,s,a,l,u,m,g;return b().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(i=r.privacy_declarations.filter((function(e){return e.consent_use!==P.consent_use})).flatMap((function(e){var r=e.cookieNames.map((function(r){var t=e.cookies.find((function(e){return e.name===r}));return null!==t&&void 0!==t?t:{name:r,path:"/"}})),t=(e.cookieNames,e.consent_use,(0,f.Z)(e,G));return"marketing"!==e.consent_use||e.data_use?H(H({},t),{},{data_use:e.data_use?e.data_use:e.consent_use,cookies:r}):["marketing.advertising.first_party.targeted","marketing.advertising.third_party.targeted"].map((function(e){return H(H({},t),{},{data_use:e,cookies:r})}))})),o=t?t.privacy_declarations.filter((function(e){return!E(e.data_use)})):[],s=t?[].concat((0,p.Z)(o),(0,p.Z)(i)):i,a=d.find((function(e){return e.value===r.vendor_id})),l=a?a.value:void 0,u=r.name,a?u=a.label:r.vendor_id&&(u=r.vendor_id),m={vendor_id:l,name:t?t.name:u,fides_key:t?t.fides_key:(0,D.E)(u),system_type:t?t.system_type:"",privacy_declarations:s},!t){e.next=14;break}return e.next=11,S(m);case 11:e.t0=e.sent,e.next=17;break;case 14:return e.next=16,h(m);case 16:e.t0=e.sent;case 17:if(g=e.t0,!(0,z.D4)(g)){e.next=21;break}return c((0,R.Vo)((0,z.e$)(g.error))),e.abrupt("return");case 21:c((0,R.t5)("Vendor successfully ".concat(t?"updated":"created","!"))),n.resetForm(),M();case 24:case"end":return e.stop()}}),e)})));return function(r,t){return e.apply(this,arguments)}}(),X=l?$:q;return(0,A.jsxs)(A.Fragment,{children:[(0,A.jsx)(j.zx,{onClick:s.onOpen,"data-testid":"add-vendor-btn",size:"sm",colorScheme:"primary",children:"Add vendor"}),(0,A.jsx)(O.J9,{initialValues:W,enableReinitialize:!0,onSubmit:I,validationSchema:X,children:function(e){var r,i=e.dirty,o=e.values,a=e.isValid,c=e.resetForm;return d.every((function(e){return e.value!==o.vendor_id}))?r="disabled":B&&(r="showing"),(0,A.jsx)(F,{isOpen:s.isOpen,onClose:s.onClose,title:t?"Edit vendor":"Add a vendor",onSuggestionClick:function(){V(!0)},suggestionsState:r,children:(0,A.jsx)(n.xu,{"data-testid":"add-vendor-modal-content",my:4,children:(0,A.jsx)(O.l0,{children:(0,A.jsxs)(n.gC,{alignItems:"start",spacing:6,children:[l?(0,A.jsx)(w.VT,{id:"vendor",name:"vendor_id",label:"Vendor",placeholder:"Select a vendor",singleValueBlock:!0,options:d,tooltip:"Select the vendor that matches the system",isCustomOption:!0,variant:"stacked",isDisabled:!!t,isRequired:!0}):null,t&&!t.vendor_id||!l?(0,A.jsx)(w.j0,{id:"name",name:"name",isRequired:!0,label:"Vendor name",tooltip:"Give the system a unique, and relevant name for reporting purposes. e.g. \u201cEmail Data Warehouse\u201d",variant:"stacked",disabled:!!t}):null,(0,A.jsx)(L,{showSuggestions:B}),(0,A.jsxs)(j.hE,{size:"sm",width:"100%",justifyContent:"space-between",children:[(0,A.jsx)(j.zx,{variant:"outline",onClick:function(){M(),c()},children:"Cancel"}),(0,A.jsx)(j.zx,{type:"submit",variant:"primary",isDisabled:u||!i||!a,isLoading:u,"data-testid":"save-btn",children:"Save vendor"})]})]})})})})}})]})},K=t(29470),Q=t(5008),Y=t(40240),J=t(60378),ee=t(55447),re=t(95319),te=t(82466),ne=t(99725),ie=t(85249);function oe(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function se(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?oe(Object(t),!0).forEach((function(r){(0,v.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):oe(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var ae=function(e){(0,V.fd)();var r=(0,C.C)(V.U3),t=new Map(r.map((function(e){return[e.fides_key,e.name||e.fides_key]})));return"N/A"===e.value?(0,A.jsx)(n.xu,{p:2,children:"N/A"}):(0,A.jsx)(n.xu,{children:(0,A.jsx)(re.N0,se({isPlainText:!0,map:t},e))})};function ce(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);r&&(n=n.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,n)}return t}function le(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?ce(Object(t),!0).forEach((function(r){(0,v.Z)(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):ce(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}var ue=function(){var e,r,t=(0,C.C)(N.cS),i=(0,a.useMemo)((function(){return function(e){var r=[];return e.forEach((function(e){var t=!1,n=e.privacy_declarations.map((function(e){return{cookies:e.cookies,dataUse:e.data_use}}));n.length&&n.forEach((function(n){var i=n.dataUse,o=n.cookies;null===o||void 0===o||o.forEach((function(n){t=!0,r.push({cookie:n,name:e.name,id:e.fides_key,dataUse:i})}))})),t||r.push({name:e.name,id:e.fides_key})})),r}(t)}),[t]),o=(0,a.useState)(void 0),s=o[0],c=o[1],l=(0,a.useState)(void 0),u=l[0],d=l[1],p=(0,y.qY)(),f=p.isOpen,v=p.onOpen,h=p.onClose,O=(0,a.useMemo)((function(){return[{Header:"Vendor",accessor:"name",Cell:re.p7,aggregate:function(e){return e[0]}},{Header:"Id",accessor:"id"},{Header:"Cookie name",accessor:function(e){return e.cookie?e.cookie.name:"N/A"},Cell:re.p7},{Header:"Data use",accessor:function(e){var r;return null!==(r=e.dataUse)&&void 0!==r?r:"N/A"},Cell:ae}]}),[]),_=(0,J.useTable)({columns:O,data:i,initialState:{groupBy:["id"],hiddenColumns:["id"]}},J.useGlobalFilter,J.useGroupBy,J.useFlexLayout,J.useResizeColumns),k=_.getTableProps,w=_.getTableBodyProps,P=_.headerGroups,S=_.prepareRow,E=_.rows,D=(0,N.DW)(),Z=(0,g.Z)(D,1)[0],T=(0,x.pm)(),B=function(){var e=(0,m.Z)(b().mark((function e(r){var t;return b().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Z(r);case 2:t=e.sent,(0,z.D4)(t)?T((0,R.Vo)((0,z.e$)(t.error))):T((0,R.t5)("Successfully deleted vendor")),h();case 5:case"end":return e.stop()}}),e)})));return function(r){return e.apply(this,arguments)}}();return(0,A.jsxs)(n.xu,{boxSize:"100%",overflow:"auto",children:[(0,A.jsxs)(n.Ug,{mt:2,mb:4,justifyContent:"space-between",children:[(0,A.jsx)(ie.Z,{globalFilter:_.state.globalFilter,setGlobalFilter:_.setGlobalFilter,placeholder:"Search"}),(0,A.jsx)(X,{passedInSystem:s,onCloseModal:function(){return c(void 0)}}),(0,A.jsx)(ee.Z,{isOpen:f,onClose:h,onConfirm:function(){return B(u.fides_key)},title:"Delete ".concat(null!==(e=null===u||void 0===u?void 0:u.name)&&void 0!==e?e:null===u||void 0===u?void 0:u.fides_key),message:(0,A.jsxs)(A.Fragment,{children:[(0,A.jsxs)(n.xv,{children:["This will delete the vendor"," ",(0,A.jsx)(n.xv,{color:"complimentary.500",as:"span",fontWeight:"bold",children:null!==(r=null===u||void 0===u?void 0:u.name)&&void 0!==r?r:null===u||void 0===u?void 0:u.fides_key})," ","and all its cookies."]}),(0,A.jsx)(n.xv,{children:"Are you sure you want to continue?"})]})})]}),(0,A.jsxs)(Y.iA,le(le({},k()),{},{size:"sm","data-testid":"datamap-table",children:[(0,A.jsx)(ne.Z,{headerGroups:P}),(0,A.jsx)(te.Z,{rows:E,renderRowSubheading:function(e){return e.values.name},prepareRow:S,getTableBodyProps:w,renderOverflowMenu:function(e){return(0,A.jsxs)(K.v2,{children:[(0,A.jsx)(K.j2,{as:j.hU,"aria-label":"Show vendor options",icon:(0,A.jsx)(Q.nX,{}),size:"xs",variant:"outline","data-testid":"configure-".concat(e.values.id)}),(0,A.jsxs)(K.qy,{children:[(0,A.jsx)(K.sN,{"data-testid":"edit-".concat(e.values.id),onClick:function(){return function(e){var r=t.find((function(r){return e===r.fides_key}));c(r)}(e.values.id)},children:"Manage cookies"}),(0,A.jsx)(K.sN,{"data-testid":"delete-".concat(e.values.id),onClick:function(){return function(e){var r=t.find((function(r){return e===r.fides_key}));d(r),v()}(e.values.id)},children:"Delete"})]})]})}})]}))]})},de=function(){return(0,A.jsxs)(n.gC,{spacing:4,alignItems:"start",children:[(0,A.jsx)(n.xv,{children:"To manage consent, please add your first vendor. A vendor is a third-party SaaS application that processes personal data for varying purposes."}),(0,A.jsx)(X,{})]})},pe=function(){var e=(0,N.K3)(),r=e.data,t=e.isLoading;return(0,V.fd)(),t?(0,A.jsx)(n.M5,{children:(0,A.jsx)(u.$,{})}):r&&0!==r.length?(0,A.jsx)(ue,{}):(0,A.jsx)(d.Z,{title:"It looks like it's your first time here!",description:(0,A.jsx)(de,{})})},fe=function(){return(0,A.jsxs)(c.Z,{title:"Configure consent",children:[(0,A.jsxs)(n.xu,{mb:4,children:[(0,A.jsx)(n.X6,{fontSize:"2xl",fontWeight:"semibold",mb:2,"data-testid":"header",children:"Configure consent"}),(0,A.jsx)(n.xu,{children:(0,A.jsxs)(i.aG,{fontWeight:"medium",fontSize:"sm",color:"gray.600","data-testid":"breadcrumbs",children:[(0,A.jsx)(i.gN,{children:(0,A.jsx)(s(),{href:l.zo,children:"Consent"})}),(0,A.jsx)(i.gN,{color:"complimentary.500",children:(0,A.jsx)(s(),{href:"#",children:"Configure consent"})})]})})]}),(0,A.jsx)(n.xv,{fontSize:"sm",mb:8,width:{base:"100%",lg:"50%"},children:"Your current cookies and tracking information."}),(0,A.jsx)(n.xu,{"data-testid":"configure-consent-page",children:(0,A.jsx)(pe,{})})]})}},54727:function(e,r,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/consent/configure",function(){return t(96085)}])}},function(e){e.O(0,[2141,845,8301,8194,9,5232,4968,9774,2888,179],(function(){return r=54727,e(e.s=r);var r}));var r=e.O();_N_E=r}]);