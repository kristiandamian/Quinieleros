using System;

namespace Quinieleros.Ligas
{
	public class SanLuis:EquipoMexico
	{
		public SanLuis ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los tuneros", "Los potosinos", "El Átletico" };
			this.Nombre = "San Luis";
			this.Icon = "";
			this.id = "SANLUIS";
		}
	}
}

