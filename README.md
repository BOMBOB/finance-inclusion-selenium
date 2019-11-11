export PATH="$(pwd):$PATH" 

ีอันนี้คือวิธีที่คิดคร่าวๆกัน กับพี่เกมพี่เคีลยร์พี่รี่ฮะ เขียนแบบนี้โอเคไหม เหมาะสมไหมในแต่ละหัวข้อ

text of image 
คือดูว่าใน web นั้นประกอบไปด้วย pdf ไหม ถ้ามีpdf แปลว่าไม่ดี
F12 > search pdf > ถ้ามี หักแต้มควรใช้เป็น text แทน

Scolling
- check จาก width หรือ max-width แต่ควรเป็น "%"  ถ้าเป็น px ไม่โอเค
- check ว่ามี grid - container มั้ย  grid-template-columns เหมือนช่วยจัดการ layout ให้จาก grid
- check flex คือ flex จะช่วยให้หน้าจอ flexible ขึ้น
-  ถ้ามี long URL ก็ check overflow-wrap: break-word หรือ word-wrap: break-word มันจะ wrap URL ให้
- ถ้ามีรูป แล้วจะ fit image ก็ check max-width หรือ height ควรเป็น "%"

Target size
ดึง tag เหล่านี้ และดู css ของ tag เหล่านี้มีอะไรบ้าง
- extract: จาก tag <a>, <button>, <input type="submit">, onclick, onchange, onmouse..., hover, on...
เช็ค css ใน cursor ว่าควรเป็นสัญลักษณ์ที่บ่งบอกว่าเป็นลิงค์
- cursor: ใช้ onclick window.location ให้ redirect ไปหน้าอื่น แต่ไม่ได้ set cursor:pointer ทำให้ user ไม่รู้ว่าข้อความนี้เป็น link
เช็ค css ข้อความกับสี มีความเชื่อมโยง (ยังไม่รู้ว่าจะเช็คไง)
- color: ดูว่าสีของปุ่มสื่อความหมายหรือไม่ เช่น ตกลง=สีเขียว, ยกเลิก=สีแดง
เช็ค css ดู ratio ของ tag ข้างๆกันว่ามีขนาดห่างกันมากเกินไปไหม ถ้ามากเกินอาจทำให้สายตาเรา mislead มองไม่เห็นอีก targetได้
- position: ลิ้งค์สำคัญๆอยู่ในตำแหน่งที่มองเห็นได้ง่ายหรือไม่
ไม่ควรเปิด tab ใหม่ตลอดในทุกๆลิ้งค์
- tab: ดู target="__blank", window.open ถ้าเยอะไปไม่น่าจะดี
ควรมี alert ใน target ที่มีความสำคัญ
- alert: เมื่อคลิกปุ่ม ก่อนที่จะ action อะไรสักอย่างควรมี alert เช่น Are you sure you want to delete?

Text space
ใน case เหล่านี้ควร มี condition: Padding > font size 30%
(ยังหาวิธีดูรอบๆ text อยู่)

Case1 
  padding-top: 50px;
  padding-right: 30px;
  padding-bottom: 50px;
  padding-left: 80px;

Case2
padding: 25px 50px 75px 100px;
* top padding is 25px
* right padding is 50px
* bottom padding is 75px
* left padding is 100px

Case3
padding: 25px 50px 75px;
* top padding is 25px
* right and left paddings are 50px
* bottom padding is 75px

Case4
padding: 25px 50px;
* top and bottom paddings are 25px
* right and left paddings are 50px

Case5
padding: 25px;
* all four paddings are 25px