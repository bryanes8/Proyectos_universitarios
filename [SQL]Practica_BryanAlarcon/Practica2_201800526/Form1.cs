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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btnProductos_Click(object sender, EventArgs e)
        {
            Form formularioT = new Form2();
            formularioT.Show();
        }

        private void btnEmpleados_Click(object sender, EventArgs e)
        {
            Form formularioE = new Empleados();
            formularioE.Show();
        }

        private void btnTiendas_Click(object sender, EventArgs e)
        {
            Form formularioT = new Tiendas();
            formularioT.Show();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }
    }
}
