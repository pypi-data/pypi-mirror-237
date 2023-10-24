/*!
 * Quasar Framework v2.13.0
 * (c) 2015-present Razvan Stoenescu
 * Released under the MIT License.
 */
(function(a,e){"object"===typeof exports&&"undefined"!==typeof module?module.exports=e():"function"===typeof define&&define.amd?define(e):(a="undefined"!==typeof globalThis?globalThis:a||self,a.Quasar=a.Quasar||{},a.Quasar.lang=a.Quasar.lang||{},a.Quasar.lang.my=e())})(this,function(){"use strict";var a={isoName:"my",nativeName:"Malaysia",label:{clear:"kosong",ok:"pasti",cancel:"Batal",close:"penutupan",set:"sediakan",select:"pilih",reset:"set semula",remove:"keluarkan",update:"memperbaharui",create:"cipta",search:"cari",filter:"penapis",refresh:"segarkan semula",expand:a=>a?`"${a}" ko hkyaae htwin par`:"hkyaae htwin par",collapse:a=>a?`"${a}" ko hkout saimpar`:"pyaokya sai"},date:{days:"Ahad_Isnin_Selasa_Rabu_Khamis_Jumaat_Sabtu".split("_"),daysShort:"Aha_Isn_Sel_Rab_Kha_Jum_Sab".split("_"),months:"Januari_Februari_Mac_April_Mei_Jun_Julai_Ogos_September_Oktober_November_Disember".split("_"),monthsShort:"Jan_Feb_Mac_Apr_Mei_Jun_Jul_Ogo_Sep_Okt_Nov_Dis".split("_"),headerTitle:a=>new Intl.DateTimeFormat("my",{weekday:"short",month:"short",day:"numeric"}).format(a),firstDayOfWeek:0,format24h:!1,pluralDay:"langit"},table:{noData:"tiada data tersedia",noResults:"Tiada data yang sepadan ditemui",loading:"memuatkan...",selectedRecords:a=>"dipilih"+a+"baris",recordsPerPage:"baris setiap muka surat:",allRows:"semua",pagination:(a,e,n)=>a+"-"+e+" / "+n,columns:"Senaraikan"},editor:{url:"URL",bold:"berani",italic:"condong",strikethrough:"tembus",underline:"gariskan",unorderedList:"senarai tidak teratur",orderedList:"senarai pesanan",subscript:"subskrip",superscript:"superskrip",hyperlink:"Hiperpautan",toggleFullscreen:"togol skrin penuh",quote:"tanda petikan",left:"Jajar ke kiri",center:"penjajaran tengah",right:"Sejajar ke kanan",justify:"wajar",print:"Cetak",outdent:"mengurangkan lekukan",indent:"meningkatkan inden",removeFormat:"gaya yang jelas",formatting:"format",fontSize:"Saiz huruf",align:"selaraskan",hr:"Masukkan garisan mendatar",undo:"membatalkan",redo:"buat semula",heading1:"Tajuk satu",heading2:"Tajuk dua",heading3:"Tajuk tiga",heading4:"Tajuk Empat",heading5:"Tajuk Lima",heading6:"Tajuk Enam",paragraph:"perenggan",code:"kod",size1:"sangat kecil",size2:"lebih kecil",size3:"biasa",size4:"sederhana hingga besar",size5:"besar",size6:"sangat besar",size7:"super besar",defaultFont:"fon lalai",viewSource:"menyemak data"},tree:{noNodes:"tiada nod tersedia",noResults:"Tiada nod yang sepadan ditemui"}};return a});