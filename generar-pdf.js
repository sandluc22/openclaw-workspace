const PDFDocument = require('pdfkit');
const fs = require('fs');

const doc = new PDFDocument({
  layout: 'portrait',
  size: 'A4',
  margins: { top: 50, bottom: 50, left: 50, right: 50 }
});

const stream = fs.createWriteStream('/home/node/workspace/sandra-galilea/guia/guia-3-errores.pdf');
doc.pipe(stream);

// --- PORTADA ---
doc.rect(0, 0, doc.page.width, doc.page.height).fill('#f8f9fa');

doc.rect(50, 80, doc.page.width - 100, 3).fill('#3b82f6');
doc.rect(50, 82, doc.page.width - 100, 1).fill('#bfdbfe');
doc.rect(50, 83, doc.page.width - 100, 1).fill('#bfdbfe');

doc.fillColor('#3b82f6').fontSize(12).font('Helvetica-Bold')
   .text('GUÍA GRATUITA', 50, 100, { align: 'center' });

doc.fillColor('#1f2937').fontSize(24).font('Helvetica-Bold')
   .text('Los 3 errores que todo autónomo', 50, 130, { align: 'center', width: doc.page.width - 100 });
doc.fillColor('#2563eb').fontSize(24).font('Helvetica-Bold')
   .text('comete con sus seguros', 50, 162, { align: 'center', width: doc.page.width - 100 });

doc.fillColor('#6b7280').fontSize(12).font('Helvetica')
   .text('Y cómo solucionarlos en menos de 10 minutos, sin compromiso ni letra pequeña.', 50, 210, { align: 'center', width: doc.page.width - 100 });

doc.fillColor('#1f2937').fontSize(11).font('Helvetica')
   .text('colaboradores de Grupo Galilea', 50, 270, { align: 'center', width: doc.page.width - 100 });
doc.fillColor('#9ca3af').fontSize(9).font('Helvetica')
   .text('Colaboradores · Madrid · Toda España', 50, 288, { align: 'center', width: doc.page.width - 100 });

doc.rect(50, 340, doc.page.width - 100, 2).fill('#3b82f6');

doc.addPage();

// --- INTRO ---
doc.fillColor('#1f2937').fontSize(11).font('Helvetica-Bold')
   .text('Hola, somos el equipo de colaboradores de Grupo Galilea.', 50, 60, { width: doc.page.width - 100 });

doc.fillColor('#4b5563').fontSize(10).font('Helvetica')
   .text('Somos un equipo en Madrid y ayudamos a autónomos y empresas a proteger su patrimonio. Llevamos tiempo viendo cómo muchos autónomos cometen los mismos errores con sus seguros, y hemos escrito esta guía para que no te pille desprevenido.', 50, 90, { width: doc.page.width - 100 });

doc.text('Aquí van los tres errores más habituales — y cómo evitarlos fácilmente.', 50, 150, { width: doc.page.width - 100 });

function addError(num, title, body, solution) {
  doc.addPage();
  
  // Error number badge
  doc.rect(50, 55, 28, 28).fill('#3b82f6');
  doc.fillColor('#ffffff').fontSize(14).font('Helvetica-Bold')
     .text(num, 50, 59, { width: 28, align: 'center' });
  
  doc.fillColor('#1f2937').fontSize(16).font('Helvetica-Bold')
     .text(title, 88, 58, { width: doc.page.width - 138 });
  
  doc.fillColor('#4b5563').fontSize(10).font('Helvetica')
     .text(body, 50, 105, { width: doc.page.width - 100 });
  
  // Solution box
  doc.rect(50, doc.y + 20, doc.page.width - 100, 1).fill('#bfdbfe');
  doc.fillColor('#2563eb').fontSize(11).font('Helvetica-Bold')
     .text('✅ Solución:', 50, doc.y + 35, { width: doc.page.width - 100 });
  doc.fillColor('#1f2937').fontSize(10).font('Helvetica')
     .text(solution, 50, doc.y + 5, { width: doc.page.width - 100 });
}

addError(1, 'Contratar el seguro más barato y olvidarse',
  'Muchos autónomos contratan la póliza mínima exigida por ley o el seguro más barato que encuentran, lo firman y no lo vuelven a mirar nunca. El problema es que cuando ocurre un siniestro, descubren que lo que necesitan no está cubierto.\n\nUn ejemplo clásico: un autónomo que tiene un seguro de responsabilidad civil general, pero su actividad real implica riesgos específicos que no están incluidos. Cuando tiene un problema, el seguro no responde.',
  'Revisa tus pólizas una vez al año. Pregunta específicamente qué cubre y qué no cubre cada seguro. A veces por 10-15€ más al mes tienes una cobertura que multiplica tu tranquilidad.'
);

addError(2, 'No aprovechar los planes de ahorro como autónomo',
  'Como autónomo, tienes ventajas fiscales que los empleados por cuenta ajena no tienen. Una de las más potentes: los planes de ahorro y previsión.\n\nPuedes deducirte hasta 5.500€ anuales en tu IRPF si aportas a un plan de ahorro sistemático. Es decir, no solo estás ahorrando para tu futuro, sino que además pagas menos impuestos ese año.\n\nLa mayoría de autónomos no lo sabe o lo deja para "más adelante" y se pierde cientos de euros en deducciones cada año.',
  'Con un plan de ahorro adaptado a tu facturación, puedes ahorrar para tu jubilación y reducir tu factura fiscal al mismo tiempo. No necesitas grandes cantidades: desde 50€ al mes ya tiene sentido.'
);

addError(3, 'Mezclar seguros personales con los del negocio',
  'Muchos autónomos usan su seguro de hogar para cubrir material del trabajo, o dan por hecho que su seguro de vida personal cubre también su actividad profesional. Error.\n\nSi trabajas desde casa y tienes un seguro de hogar estándar, tus equipos informáticos, herramientas o existencias no están cubiertos si sufren un robo o un desperfecto.\n\nTener separado lo personal de lo profesional no es un capricho — es una necesidad para no llevarte sorpresas.',
  'Pide un análisis conjunto de tus coberturas. Muchas veces se puede contratar un seguro multirriesgo para autónomos que cubra tu actividad sin pagar por duplicidades. Cuesta menos de lo que piensas.'
);

// --- PÁGINA DE CIERRE ---
doc.addPage();

doc.fillColor('#1f2937').fontSize(16).font('Helvetica-Bold')
   .text('📌 En resumen', 50, 60, { width: doc.page.width - 100 });

doc.fillColor('#4b5563').fontSize(11).font('Helvetica')
   .text('✅ Revisa tus seguros cada año — no los contrates y olvides.', 50, 100, { width: doc.page.width - 100 });
doc.text('✅ Aprovecha los planes de ahorro para deducir impuestos siendo autónomo.', 50, 130, { width: doc.page.width - 100 });
doc.text('✅ Separa tus coberturas personales de las profesionales.', 50, 160, { width: doc.page.width - 100 });

// CTA Box
doc.rect(50, 210, doc.page.width - 100, 140).fill('#1f2937');

doc.fillColor('#ffffff').fontSize(14).font('Helvetica-Bold')
   .text('🤝 ¿Quieres revisar tu situación?', 70, 230, { width: doc.page.width - 140 });

doc.fillColor('#d1d5db').fontSize(10).font('Helvetica')
   .text('Sin compromiso y sin presión. Te ayudamos a ver si estás cubierto donde importa y si puedes ahorrar en impuestos con un plan de ahorro.', 70, 260, { width: doc.page.width - 140 });

doc.fillColor('#3b82f6').fontSize(9).font('Helvetica')
   .text('crecimientofinancieroglobal@gmail.com', 70, 310, { width: doc.page.width - 140 });

// Footer
doc.fillColor('#9ca3af').fontSize(7).font('Helvetica')
   .text('© 2026 Crecimiento Financiero Global · colaboradores de Grupo Galilea · Madrid · Toda España', 50, doc.page.height - 40, { align: 'center', width: doc.page.width - 100 });
doc.text('Esta guía tiene fines informativos. Consulta tu caso particular con un profesional.', 50, doc.page.height - 25, { align: 'center', width: doc.page.width - 100 });

doc.end();

stream.on('finish', () => {
  const stats = fs.statSync('/home/node/workspace/sandra-galilea/guia/guia-3-errores.pdf');
  console.log('✅ PDF generado correctamente');
  console.log('📄 Tamaño:', (stats.size / 1024).toFixed(1), 'KB');
  console.log('📍', '/home/node/workspace/sandra-galilea/guia/guia-3-errores.pdf');
});
