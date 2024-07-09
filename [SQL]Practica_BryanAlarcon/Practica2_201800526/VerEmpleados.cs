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
    public partial class VerEmpleados : Form
    {
        public VerEmpleados()
        {
            InitializeComponent();
        }

        private void VerEmpleados_Load(object sender, EventArgs e)
        {
            Conexion c = new Conexion();
            c.CargarEmpleado(dgvVerEmpleados);
        }
    }
}
