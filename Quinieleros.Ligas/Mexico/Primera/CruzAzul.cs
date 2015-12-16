using System;

namespace Quinieleros.Ligas
{
	public class CruzAzul : EquipoMexico
	{
		public CruzAzul ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "La máquina", "Los Cementeros" };
			this.Nombre = "Cruz Azul";
			this.Icon = "";
			this.id = "CRUZAZUL";
		}
	}
}

