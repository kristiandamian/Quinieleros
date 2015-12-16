using System;

namespace Quinieleros.Ligas
{
	public class UdG: EquipoMexico
	{
		public UdG ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los Leones Negros", "Los melenudos" };
			this.Nombre = "U. de G.";
			this.Icon = "";
			this.id = "UDG";
		}
	}
}

