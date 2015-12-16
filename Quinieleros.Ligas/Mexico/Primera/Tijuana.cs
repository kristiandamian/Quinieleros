using System;

namespace Quinieleros.Ligas
{
	public class Tijuana:EquipoMexico
	{
		public Tijuana ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los Xolos","La jauria", "El Xolaje" };
			this.Nombre = "Tijuana";
			this.Icon = "";
			this.id = "TIJUANA";
		}
	}
}

