namespace Practica2_201800526
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnProductos = new System.Windows.Forms.Button();
            this.btnEmpleados = new System.Windows.Forms.Button();
            this.btnTiendas = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnProductos
            // 
            this.btnProductos.Location = new System.Drawing.Point(70, 71);
            this.btnProductos.Name = "btnProductos";
            this.btnProductos.Size = new System.Drawing.Size(93, 35);
            this.btnProductos.TabIndex = 0;
            this.btnProductos.Text = "Productos";
            this.btnProductos.UseVisualStyleBackColor = true;
            this.btnProductos.Click += new System.EventHandler(this.btnProductos_Click);
            // 
            // btnEmpleados
            // 
            this.btnEmpleados.Location = new System.Drawing.Point(70, 124);
            this.btnEmpleados.Name = "btnEmpleados";
            this.btnEmpleados.Size = new System.Drawing.Size(93, 35);
            this.btnEmpleados.TabIndex = 1;
            this.btnEmpleados.Text = "Empleados";
            this.btnEmpleados.UseVisualStyleBackColor = true;
            this.btnEmpleados.Click += new System.EventHandler(this.btnEmpleados_Click);
            // 
            // btnTiendas
            // 
            this.btnTiendas.Location = new System.Drawing.Point(70, 180);
            this.btnTiendas.Name = "btnTiendas";
            this.btnTiendas.Size = new System.Drawing.Size(93, 35);
            this.btnTiendas.TabIndex = 2;
            this.btnTiendas.Text = "Tiendas";
            this.btnTiendas.UseVisualStyleBackColor = true;
            this.btnTiendas.Click += new System.EventHandler(this.btnTiendas_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(76, 27);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(77, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "Menú Principal";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(241, 239);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnTiendas);
            this.Controls.Add(this.btnEmpleados);
            this.Controls.Add(this.btnProductos);
            this.Name = "Form1";
            this.Text = "Menú Principal";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnProductos;
        private System.Windows.Forms.Button btnEmpleados;
        private System.Windows.Forms.Button btnTiendas;
        private System.Windows.Forms.Label label1;
    }
}

