using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Practica2_201800526
{
    public partial class VerProducto : Form
    {
      
        public VerProducto()
        {
            InitializeComponent();
        }

        private void VerProducto_Load(object sender, EventArgs e)
        {
            Conexion c = new Conexion();
            c.CargarProducto(dgvVerPersona);
        }
    }
}
